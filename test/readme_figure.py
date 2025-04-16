"""Create a nice figure for the README"""

import bramplot as plt
from bramplot.presets import PRESETS
import numpy as np
import catppuccin
from catppuccin.extras.matplotlib import get_colormap_from_list
from pathlib import Path

np.random.seed(1)

def get_simulated_data():
    # Coordinate grid
    N = 500
    x = np.linspace(-1, 1, N)
    y = np.linspace(-1, 1, N)
    X, Y = np.meshgrid(x, y)

    # Radial distance
    R = np.sqrt(X**2 + Y**2)

    # Mountain shape: central peak with exponential decay
    Z = np.zeros_like(R)

    # Add smaller bumps
    for _ in range(50):
        cx, cy = np.random.uniform(-1, 1, 2)
        bump = np.exp(-((X - cx)**2 + (Y - cy)**2) * 10)
        Z += bump * np.random.uniform(-0.5, 0.5)

    Z[Z<-1] = -1
    Z[Z>1] = 1

    return X, Y, Z*100

fig, axes = plt.subplot_mosaic("abc", width_ratios = [1.618, 1, 0.1])

width, _, font = PRESETS["latex_double_column"]

# I have one line plot, which I want to be golden ratio, and one square
# image plot. So the widths are 1.618+1, with 0.1 added for the colorbar.
height = width / (1+1.618+0.1)

cmap = get_colormap_from_list("latte", ["blue", "base", "green"])

X, Y, Z = get_simulated_data()

# Plot line profiles
slices = [300, 100]
colors = [catppuccin.PALETTE.latte.colors.red.hex, catppuccin.PALETTE.latte.colors.yellow.hex]
for slice, color in zip(slices, colors):
    axes["a"].plot(X[slice], Z[slice], label=f"Vertical distance = {Y[slice, 0]:.2f} km", color=color)
    axes["b"].axhline(Y[slice, 0], color=color, linestyle="--", linewidth=2)
axes["a"].set_xlabel("Horizontal distance (km)")
axes["a"].set_ylabel("Height above sea level (m)")
axes["a"].set_ylim([-100, 100])
axes["a"].legend()

# Plot color map of the simulated map
cs = axes["b"].contourf(X, Y, Z, cmap=cmap, vmin=-100, vmax=100)
axes["b"].contour(cs, colors=catppuccin.PALETTE.latte.colors.text.hex)
axes["b"].set_xlabel("Horizontal distance (km)")
axes["b"].set_ylabel("Vertical distance (km)")
axes["b"].set_xticks([-1, 0, 1])
axes["b"].set_yticks([-1, 0, 1])
plt.colorbar(cs, cax=axes["c"], ax=axes["b"], label="Height above sea level (m)")

plt.set_size(width, height, font)

save_dir = Path(__file__).parent.parent / "images"
fig.savefig(save_dir / "island_profile.png")
