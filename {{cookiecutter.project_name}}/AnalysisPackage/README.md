Example EventLoop Analysis Package
==================================

This is a very simple demonstration of a package that builds EventLoop algorithm
code for an analysis. You should compose your analysis repository of one or
multiple ones of such packages.

The package builds a single algorithm that produces a very simple histogram on
its output, and provides a (Python) run script that executes a job locally using
this algorithm.

You can run the example job simply with:

```
AnalysisJob_run.py
```

If you don't want to use the default input file for the job, you can specify
which file to run over, using:

```
AnalysisJob_run.py --input-files=/some/DAOD.pool.root
```

**Note:** Executing the script is unfortunately a bit more awkward on MacOS.
There you need to run it with:

```
python `which AnalysisJob_run.py` --input-files=/some/DAOD.pool.root
```
