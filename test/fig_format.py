"""Example for the .fig format"""

from plot import plot
import bramplot as plt
from pathlib import Path

save_dir = Path(__file__).parent.parent / "images"

fig = plot()
fig.savefig(save_dir / "fig_format_before", format=["png","fig"])

fig = plt.load(save_dir / "fig_format_before.fig")
plt.title("New title and size")
plt.set_size(width=2.5, aspect="square")
fig.savefig(save_dir / "fig_format_after.png")
