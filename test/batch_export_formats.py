"""Script to test batch exporting of figure formats"""

from plot import plot
import bramplot as plt

fig = plot()

plt.savefig("/tmp/batch_export", format=["png", "pdf", "svg", "eps"])
