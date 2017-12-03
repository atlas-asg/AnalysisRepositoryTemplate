ATLAS Analysis Repository Template
==================================

This repository is meant to serve as a starting point when writing an
analysis project in ATLAS. And as a reference when migrating existing
analysis code into a Git repository.

Personalising The Repository
----------------------------

The template is set up using
[cookiecutter](https://cookiecutter.readthedocs.io/). To create a
project, based on the template, first you need to install that
project. You can do that with

```
pip install --user cookiecutter
```

on most platforms. (If you have super user rights for your machine,
then you can also install it as a system-wide python module of
course.) This will put the `cookiecutter` executable under
`~/.local/bin/cookiecutter` on SLC6, and under
`~/Library/Python/2.7/bin/cookiecutter` on macOS.

Once you have that executable, you can generate a project from the
template with:

```
<somewhere>/cookiecutter https://:@gitlab.cern.ch:8443/atlas-asg/AnalysisRepositoryTemplate.git
```

It will ask you some questions that you need to provide answers for,
based on the [cookiecutter.json](cookiecutter.json) file of the
template, and then generate a subdirectory (under `$PWD`) with the name
that you specified as the `project_name` variable.
