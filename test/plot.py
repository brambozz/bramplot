"""Some basic plots"""

import bramplot as plt
import numpy as np

x = np.linspace(0, 1, 50)
y = x**2

plt.plot(x, y, label="$y=x^2$")
plt.plot(1-x, y, label="$y=1-x^2$")
plt.title("Test plot")
plt.legend()

plt.savefig("/tmp/bramplot_test_plot.pdf", facecolor="#00000000")

