# {{cookiecutter.project_name}}

[![pipeline status](https://gitlab.cern.ch/{{cookiecutter.user_name}}/{{cookiecutter.project_name}}/badges/master/pipeline.svg)](https://gitlab.cern.ch/{{cookiecutter.user_name}}/{{cookiecutter.project_name}}/commits/master)

{{cookiecutter.short_descr}}

**Please update the README as appropriate!**

## Analysis Details

| Contact Person | Contact E-mail | Glance Analysis ID |
|----------------|----------------|--------------------|
| {{cookiecutter.contact_person}} | {{cookiecutter.contact_email}} | {{cookiecutter.analysis_id}} |

## Repository Information

### CMake configuration

The repository comes with its own project configuration file
([CMakeLists.txt](CMakeLists.txt)). It sets up the build of all of the
code of the repository against AnalysisBase-21.2 or AthAnalysis-21.2.
(Any version.)

To build the release project, just follow the instructions from the
[analysis software tutorial](https://twiki.cern.ch/twiki/bin/view/AtlasComputing/SoftwareTutorialBasicCMake),
performing an out-of-source build.

```
git clone http://:@gitlab.cern.ch:8443/{{cookiecutter.user_name}}/{{cookiecutter.project_name}}.git
asetup AnalysisBase,latest
mkdir build
cd build/
cmake ../{{cookiecutter.project_name}}/
make
```

### CI Configuration

The repository comes with a [.gitlab-ci.yml](.gitlab-ci.yml) file that
does the following:
  - It tests the [CMake](https://cmake.org) configuration of the
    project, and then the build of it.
  - It tests that the built results can be successfully installed, and
    can be built into an RPM file.
  - It builds a Docker image out of the compiled results, and uploads
    it to [gitlab-registry.cern.ch](gitlab-registry.cern.ch).

See [the GitLab CI documentation](https://docs.gitlab.com/ce/ci) for
details on how this configuration was constructed.

### Docker Configuration

The repository comes with a [Dockerfile](Dockerfile) that can be used
to build a [Docker](https://www.docker.com) image/container with the
compiled results of the repository.

The configuration is primarily used as part of the CI build, but you
can also use it to build an image locally, executing something like
the following in the repository's main directory.

```
docker build -t gitlab-registry.cern.ch/{{cookiecutter.user_name}}/{{cookiecutter.project_name.lower()}}:latest --compress --squash .
```

See the GitLab
[container registry](https://gitlab.cern.ch/{{cookiecutter.user_name}}/{{cookiecutter.project_name}}/container_registry)
documentation for further details.
