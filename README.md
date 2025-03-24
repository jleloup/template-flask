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
    make generate output="myApplication"
    ```
- You will get the result of Cookiecutter rendering into the `myApplication` directory.
