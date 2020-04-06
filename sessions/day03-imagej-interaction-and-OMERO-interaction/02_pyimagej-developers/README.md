# Integrating ImageJ/FIJI in Python & Working with Developmental Packages

## `pyimagej`

The audio recording for this talk can be found [here](https://youtu.be/5q4vHM0zOLk).

### Why?

* Why combine Python & ImageJ?: https://imagej.net/Python.
* Also, Python can be easier to script and automate and has a much wider image and data analysis community.

### The `pymagej` Module for Python

* GitHub: https://github.com/imagej/pyimagej
* Currently at version 0.5.0, i.e. very developmental.
* But! when it reaches version 1.0 it could be a very powerful tool.
* Interacts with an ImageJ/FIJI instance or 'gateway', i.e. like opening the ImageJ GUI.
* Allows you to run ImageJ Ops, Macros/Scripts and Plug-ins.
* Can be initialised with a specific verison of FIJI (globally reproducible), or with a local version with a special collection of packages (locally repeatible).
* Commands are not dissimilar to writing ImageJ macros or calling ImageJ Ops from other systems.
* Tutorial: https://nbviewer.jupyter.org/github/imagej/tutorials/blob/master/notebooks/1-Using-ImageJ/6-ImageJ-with-Python-Kernel.ipynb

#### The `server` Submodule

* GitHub: https://github.com/imagej/pyimagej/tree/master/imagej/server
* Interacts with an ImageJ/FIJI server, a new developmental tool from ImageJ.

### Advanced: CLIJ and `pyclij`

* Project websites: https://clij.github.io/, https://clij.github.io/clijpy/
* Allows GPU-accellerated ImageJ/FIJI functions and python-based interaction with those tool.

## Engaging with Developers and Developmental Packages

The audio recording for this talk can be found [here](https://youtu.be/IkJnV1UE7cI).

### GitHub - Commits, Releases and Issues

* Many packages, scripts and useful bits of code will be stored on GitHub (or, alternatively, Bitbucket or GitLab, which are similar).
* Commits show all changes made to a repository, who made them and when: e.g. https://github.com/imagej/imagej/commits/master
* Releases show the official, ideally stable, releases and are easy to download: e.g. https://github.com/imagej/imagej/releases
* Issues (both open and closed) are a good place to find answers to your problems and questions: e.g. https://github.com/imagej/imagej/issues?utf8=%E2%9C%93&q=is%3Aissue
* Good practice on writing issues: https://upthemes.com/blog/2014/02/writing-useful-github-issues/
* Key points: be polite, give package versions, use screenshots or copy and paste the important code (a minimal working example) and the whole error output.

### Image.sc, microForum and StackOverflow as Sources of Help

* Image.sc is the official forum for lots of scientific imaging softwares: https://forum.image.sc/t/frequently-asked-questions/18729
* It's a safe place to ask questions about these and other imaging software, including `pyimagej` and Python: e.g. https://forum.image.sc/tags/python
* Please follow the community guidelines when asking and answering questons: https://forum.image.sc/guidelines
* And please engage fully! - If you ask a question and people ask for more information, please try to provide it. If somebody answers the question please like the answer and reply so others know that worked.
* microForum is similar but covers hardware and wetware problems as well: https://forum.microlist.org/categories
* Finally, StackOverflow (and it's sibling websites) provide a much more general forum for programming and data questions: https://stackoverflow.com/questions/tagged/python

### microList and BIII as Sources of Packages

* microList, part of microForum, is a resource for light microscopy and covers conferences, courses, learning materials and packages/software: e.g. https://www.microlist.org/explore/?search_keywords=python&sort=latest
* BIII (Bioimage Informatics Search Engine) is a resource, set up by NEUBIAS, of bioimage informatics tools: http://biii.eu

## Citing Code/Packages

* Whenever you use somebody elses code, please remember to cite them!
* When you name/cite packages, please also include their version numbers.
* How you reference/cite the Python programming language is perhaps up for debate: https://academia.stackexchange.com/questions/5482/how-do-i-reference-the-python-programming-language-in-a-thesis-or-a-paper
* But most packages include information on how to cite them, and it really helps them if you. Without citations many groups struggle to get further funding and, therefore, won't exist to develop that new feature you want!
* Python/FIJI-related examples include:
  * https://scipy.org/citing.html
  * https://github.com/scikit-image/scikit-image/blob/307b4d0b3f7c3803b048e97ea6dc16a872ccd3e6/README.md (at bottom)
  * https://imagej.net/Citing
