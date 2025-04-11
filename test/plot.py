"""Example plot to test the library. Also exports default matplotlib
plot for comparison in the readme."""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

def plot():
    x = np.linspace(0, 1, 50)
    y = x**2
    sinusoid = np.sin(2*np.pi*x)

    fig = plt.figure()
    plt.plot(x, y, label="$y=x^2$")
    plt.plot(x, 1-y, label="$y=1-x^2$")
    plt.plot(x, sinusoid, label=r"$y=\sin (2\pi x)$")
    plt.xlabel(r"Time ($\mu$s)")
    plt.ylabel("Voltage (V)")
    plt.title("Test plot")
    plt.legend()

    return fig

save_dir = Path(__file__).parent.parent / "images"

fig = plot()
fig.savefig(save_dir / "matplotlib.png")

import bramplot as plt

fig = plot()
fig.savefig(save_dir / "bramplot.png")
