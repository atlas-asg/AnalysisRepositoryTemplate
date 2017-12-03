#
# Environment configuration file setting up the installed project.
#

# Set up the base environment using the base image's setup script:
source ~/analysis_release_setup.sh

# Set up the {{cookiecutter.project_name}} installation:
source /usr/{{cookiecutter.project_name}}/*/InstallArea/*/setup.sh
echo "Configured {{cookiecutter.project_name}} from: ${{cookiecutter.project_name}}_DIR"

# Set up the prompt:
export PS1='\[\033[01;35m\][bash]\[\033[01;31m\][\u {{cookiecutter.project_name}}-${{cookiecutter.project_name}}_VERSION]\[\033[01;34m\]:\W >\[\033[00m\] ';
