# Pelican Collection Demo

This is a demo site for the experimental Pelican Collection Builder system. It is heavily inspired by [Wax](https://minicomp.github.io/wax/), the minimal computing collection builder. It even uses the same demo images. Instead of Jekyll, this demo is based on the [Pelican](https://getpelican.com/) static site generator, using the [Python](https://www.python.org/) programming language and [Jinja](https://jinja.palletsprojects.com/) templates.

 The system consists of three building blocks:

1. A pelican plugin, [pelican-collection-builder](https://github.com/frederik-elwert/pelican-collection-builder), that dynamically generates pages from a CSV file and a folder with images,
2. a theme, [pelican-collection-theme](https://github.com/frederik-elwert/pelican-collection-theme), that displays them in a sensible manner, and
3. this template of how to bring the two together and configure them.


## Getting started

Pelican Collection Builder is a proof of concept and still under development. To get started, it is best to install the plugin and theme in editable mode, so that any changes are directly reflected in the project.

In these examples, we will use [uv](https://docs.astral.sh/uv/) to manage dependencies and the python environment. To follow these steps, make sure to [install](https://docs.astral.sh/uv/getting-started/installation/) it first. You are free to use other tools and adapt the workflow.

### Installation

The easiest way is to have the demo project, the plugin, and the theme side by side. You might want to create a dedicated folder for that. Open a terminal in that folder and download the components, either using `git checkout` or by downloading and unpacking the ZIP file from GitHub via _Code → Download ZIP_. If you use the ZIP files, make sure to rename the unpacked directories and remove the `-main` suffix.

Your folder should now look like this:

```
$ ls
pelican-collection-builder
pelican-collection-demo
pelican-collection-theme
```

Now change into the demo project:

```bash
cd pelican-collection-demo
```

Install the project dependencies from the _`pyproject.toml`_ file.

```bash
uv sync
```

This will install pelican, required dependencies, and plugins. It also installs `pelican-collection-builder` from the local directory in editable mode.

Now you can install the theme (also in editable mode):

```bash
uv run pelican-themes -s "$(realpath pelican-collection-theme)"
```

To build and view the demo project, you can run:

```bash
uv run invoke reserve
```

For the different options of building and publishing the project, see

```bash
uv run invoke -l
```

### Adding your content

To add your own content, you need:

1. A CSV file with metadata of your items. This goes into _`content/data/collection.csv`_. It needs to have at least these columns:
    - `pid`: A unique identifier for each item
    - `label`: A title or brief description of each item
2. A number of images corresponding to each row in the CSV file. They go into _`content/images`_. For each item, you need either
    - A single image file named _`pid.ext`_, where `pid` is the identifier from your CSV file, and `ext` is an image format like `jpg` or `png`.
    - A sub-folder named `pid`, with multiple images inside. This is useful if your object has multiple visual representations, like pages from a book, or different views of a three-dimensional object. You can choose the names of the individual images freely, but they will affect the order in which they are displayed.

When you first generate your page, resized versions of the images will be generated. This can take a long time, but usually only happen once. If you make changes to your images and want the thumbnails to be re-generated, delete the _`output`_ folder.
