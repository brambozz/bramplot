# Bramplot

## Goals

- [x] Just using `plt` as usual should give satisfying plots
- [x] Command line functionality which takes in `.tex` or `.pdf` and figures out appropriate sizes
- [x] Good default styles based on scienceplots and catppuccin
- [ ] Overwrite `plt` import and introduce extra save format `.fig`

## Level 1: replace pyplot import

If you just want a figure which looks decent out of the box, without worrying about sizes, simly replace your typical `import matplotlib.pyplot as plt` import with `import bramplot as plt`.
You can use all functions in `plt`, but the output has better defaults for colors and readability.

```py
import bramplot as plt
import numpy as np

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
```

**Standard matplotlib**

![](images/matplotlib.png)

**bramplot**

![](images/bramplot.png)

## Finding optimal figure width and text size

Ideally, the figures you export have exactly the width they will have in your document.
This way, they don't have to be resized and font sizes stay exactly how you set them in python.
Additionally, having titles and labels the same font size as the caption text looks best.
`bramplot` includes a script to determine the figure width and caption font size for a latex project.

1. Insert the default example image into your latex document, using *exactly* the following bit of latex:

```tex
\begin{figure}
    \includegraphics[width=\linewidth]{example-image-a.png}
    \caption{This text is to detect the caption.}
\end{figure}
```

2. Export the pdf.
3. Run the script:

```sh
python -m bramplot.find_sizes /path/to/file.pdf
```

## Development

For development I use a blank conda environment:

```sh
conda create -n bramplot python hatchling
```

And then install as an editable package:

```sh
conda activate bramplot
pip install --no-build-isolation -e .
```

