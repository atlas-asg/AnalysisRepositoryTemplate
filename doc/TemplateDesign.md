# Repository Template Design

The template can generate projects of 3 types:
  - Standalone projects built on top of AnalysisBase-21.2;
  - Athena projects built on top of AthAnalysis-21.2;
  - Hybrid projects that can be built on top of both AnalysisBase-21.2
    and AthAnalysis-21.2.

Since specialisations for the 3 cases go beyond what
[cookiecutter](https://cookiecutter.readthedocs.io/) provides out of
the box, the post-processing script
([post_gen_project.py](../hooks/post_gen_project.py)) takes care of
implementing the logic needed for us.

That is:
  - If a file has the postfix `.<base_release>` (where
    `<base_release>` may be `AnalysisBase`, `AthAnalysis` or
    `Hybrid`), that postfix is removed from it, and all files with the
    same "base name" but different postfixes get removed. To only keep
    the file meant for the selected project type.
  - If a file has no such postfix, then it is used in the same way in
    all specialisations.

To help with code management a bit, whenever a given file is meant to
be the same for 2 out of the 3 specialisations, we use soft links in
the template.
