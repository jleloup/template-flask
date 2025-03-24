# Install all requirements
.PHONY: requirements
requirements:
	pipx install pre-commit --force
	pre-commit install
	pre-commit install --hook-type commit-msg
	pip install -r requirements.txt

.PHONY: docker-build
docker-build:
	docker build ${APP_DIR} -t todo-app

.PHONY: docker-run
docker-run:
	docker run --rm -it -p 5000:5000 todo-app
