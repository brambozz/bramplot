import catppuccin
import matplotlib as mpl
from matplotlib.pyplot import *
import scienceplots

mpl.style.use("latte")

DEFAULT_WIDTH = 3.176
DEFAULT_HEIGHT = DEFAULT_WIDTH/1.618

settings = {
    "figure.figsize" : f"{DEFAULT_WIDTH},{DEFAULT_HEIGHT}",
    "figure.dpi" : 600,
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

    # Facecolors are white
    "axes.facecolor": "ffffff",
    "figure.facecolor": "ffffff",
    "savefig.facecolor": "ffffff",
}
rcParams.update(settings)


def set_size(width=DEFAULT_WIDTH, height=None, aspect="golden", font=None):
    fig = gcf()
    settings = {}

    # If height is not specified, use golden ratio
    if height is None:
        if aspect == "golden":
            height = width/1.618
        if aspect == "square":
            height = width

    settings["figure.figsize"] = f"{width},{height}"
    fig.set_figwidth(width)
    fig.set_figheight(height)


    if font is not None:
        settings["axes.labelsize"] = font
        settings["axes.titlesize"] = font
        settings["font.size"] = font

    rcParams.update(settings)
