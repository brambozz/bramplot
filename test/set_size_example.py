"""Demonstrating the `set_size()` function"""

import bramplot as plt
import numpy as np
from pathlib import Path
from plot import plot

save_dir = Path(__file__).parent.parent / "images"

fig = plot()

plt.set_size(width=4)
fig.savefig(save_dir / "bramplot_width_4.png")

plt.set_size(aspect="square")
fig.savefig(save_dir / "bramplot_square.png")

plt.set_size(width=3, height=1.5)
fig.savefig(save_dir / "bramplot_width_3_half_aspect.png")

plt.set_size(width=3, height=1.5, font=8)
fig.savefig(save_dir / "bramplot_width_3_half_aspect_font_8.png")
