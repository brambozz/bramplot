import catppuccin
import matplotlib as mpl
import matplotlib.pyplot as _plt
from matplotlib.figure import Figure as _Figure
from matplotlib.pyplot import *
import scienceplots
from pathlib import Path
import pickle

mpl.style.use("latte")

DEFAULT_WIDTH = 3.176
DEFAULT_HEIGHT = DEFAULT_WIDTH/1.618

# These are inspired by SciencePlots
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

        # Update current figure font sizes
        for ax in fig.axes:
            ax.title.set_fontsize(font)
            ax.xaxis.label.set_fontsize(font)
            ax.yaxis.label.set_fontsize(font)
            for label in ax.get_xticklabels() + ax.get_yticklabels():
                label.set_fontsize(font)


    rcParams.update(settings)

# Courtesy of uncle Chat, add .fig format and support for batch exporting

# Store the real original method
_original_savefig = _Figure.savefig

def _custom_savefig(self, fname, *args, format=None, **kwargs):
    fname = Path(fname)

    def save_single(outname, fmt):
        if fmt == ".fig":
            with open(outname, "wb") as f:
                pickle.dump(self, f)
        else:
            _original_savefig(self, outname, *args, format=fmt.lstrip("."), **kwargs)

    if isinstance(format, list):
        for fmt in format:
            fmt = f".{fmt}" if not fmt.startswith(".") else fmt
            outname = fname.with_suffix(fmt)
            save_single(outname, fmt)
    else:
        fmt = f".{format}" if format and not str(format).startswith(".") else str(format or fname.suffix)
        outname = fname.with_suffix(fmt)
        save_single(outname, fmt)

# Monkey-patch only once
_Figure.savefig = _custom_savefig

def load(file_path):
    with open(file_path, "rb") as f:
        return pickle.load(f)
