# Install all requirements for templating
.PHONY: requirements
requirements:
	pipx install pre-commit
	pipx install cookiecutter
	pre-commit install
	pre-commit install --hook-type commit-msg
