# Install all requirements
.PHONY: requirements
requirements:
	pipx install pre-commit --force
	pipx install cookiecutter
	pre-commit install
	pre-commit install --hook-type commit-msg

output="/tmp/template"

.PHONY: generate
generate:
	cookiecutter --output-dir "$(output)" .
