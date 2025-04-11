import catppuccin
import matplotlib as mpl
from matplotlib.pyplot import *
import scienceplots

mpl.style.use("latte")

settings = {
    "figure.figsize" : "3.176,1.963",
    "figure.constrained_layout.use" : True,

    "text.usetex": True,
    "text.latex.preamble": r'\usepackage{amsmath} \usepackage{amssymb}',
    "font.family": "serif",
    "axes.labelsize": 10,
    "axes.titlesize": 10,
    "font.size": 10,
    "legend.fontsize": 8,

    "lines.linewidth" : 1.5,
    "axes.linewidth" : 1,
    "grid.linewidth" : 0.5,

    # Remove legend frame
    "legend.frameon" : False,

    # Overwrite the catppuccin colors for text
    # Line and other plot element colors stay the same.
    "text.color": "000000",
    "axes.labelcolor": "000000",
    "xtick.labelcolor": "000000",
    "ytick.labelcolor": "000000",

    # Facecolors are white + transparent
    "axes.facecolor": "ffffff00",
    "figure.facecolor": "ffffff00",
    "savefig.facecolor": "ffffff00",
}
rcParams.update(settings)
