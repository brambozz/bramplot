# Bramplot

## Goals

- [ ] Overwrite `plt` import and introduce extra save format `.fig`
- [ ] Just using `plt` as usual should give satisfying plots
- [ ] Command line functionality which takes in `.tex` or `.pdf` and figures out appropriate sizes
- [ ] Good default styles based on scienceplots and catppuccin

## Finding out the figure width

Ideally, the figures you export have exactly the width they will have in your document.
This way, they don't have to be resized and font sizes stay exactly how you set them in python.
`bramplot` includes a script to determine the figure width for a latex project.

1. Insert an example image into your latex document, using *exactly* the following bit of latex:

```tex
\begin{figure}
    \includegraphics[width=\linewidth]{example-image-a.png}
\end{figure}
```

2. Export the pdf.
3. Run the script:

```sh
python -m bramplot.find_figure_width /path/to/file.pdf
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

