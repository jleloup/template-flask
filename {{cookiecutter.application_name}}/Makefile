.PHONY: install
install:
	mise trust
	mise install
	mise run provision

build:
	docker build -t test-app .

run:
	docker compose up --detach
