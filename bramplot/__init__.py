import catppuccin
import matplotlib as mpl
from matplotlib.pyplot import *
import scienceplots

mpl.style.use("latte")
# mpl.style.use(["science", catppuccin.PALETTE.latte.identifier])
# # mpl.style.use(["science"])

settings = {
    "figure.figsize" : "3.5,2.625",

    # Use LaTeX to write all text
    "text.usetex": True,
    "font.family": "serif",
    # Use 10pt font in plots, to match 10pt font in document
    "axes.labelsize": 9,
    "axes.titlesize": 9,
    "font.size": 9,

    # Make the legend/label fonts a little smaller
    # "legend.fontsize": 8,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,

    "axes.linewidth" : 1,
    "grid.linewidth" : 1,
    "lines.linewidth" : 1,

    # Remove legend frame
    "legend.frameon" : False,

    # Always save as 'tight'
    "savefig.bbox" : "tight",
    "savefig.pad_inches" : 0.0,
}
rcParams.update(settings)

