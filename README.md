# Pelican Collection Demo

This is a demo site for the experimental Pelican Collection Builder system. It is heavily inspired by [Wax](https://minicomp.github.io/wax/), the minimal computing collection builder. It even uses the same demo images. Instead of Jekyll, this demo is based on the [Pelican](https://getpelican.com/) static site generator, using the [Python](https://www.python.org/) programming language and [Jinja](https://jinja.palletsprojects.com/) templates.

 The system consists of three building blocks:

1. A pelican plugin, [pelican-collection-builder](https://github.com/frederik-elwert/pelican-collection-builder), that dynamically generates pages from a CSV file and a folder with images,
2. a theme, [pelican-collection-theme](https://github.com/frederik-elwert/pelican-collection-theme), that displays them in a sensible manner, and
3. this template of how to bring the two together and configure them.
