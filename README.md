# template-flask

Cookiecutter template to initialize a Flask project.

## Provides

This template will initiate the following components:

- a boilerplate Flask application
- a multi-stage Dockerfile to build this application as a container
- a Skaffold file to run this application in a Kubernetes environment (*optional*)

## Usage

Use the following commands to create an application out of this template:

- Update the **cookiecutter.json** file to your liking: set an application name and description, etc...
- Get into the directory you want the template to be generated in and run cookiecutter:

    ```shell
    cookiecutter <PATH_TO_THIS_REPOSITORY> <PATH_FOR_YOUR_APP>

    # Example
    cookiecutter ~/git/template-flask ~/myAPplication
    ```
- You will get the result of Cookiecutter rendering into the `myApplication` directory in your HOME directory.

Then you can use the Makefile created into the rendered application for:

- setting up your local environment to work on the app: `make install`
- building the docker container: `make build`
- locally run this container alongside a database through Docker Compose: `make run`

Warning: this application template uses Mise as a tool management to install all other tools the project may need, such as UV for Python Dependency management.
You will need Mise to install & work on the project locally.
