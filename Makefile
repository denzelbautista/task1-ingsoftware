IMAGE_NAME = geoapi:1

.DEFAULT_GOAL := help

help: ## Display available commands in Makefile
	@grep -hE '^[a-zA-Z_0-9-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

server_run: ## runs the server
	docker run --user $(shell id -u):$(shell id -g) -v $(shell pwd):/app -p 5000:5000 $(IMAGE_NAME)  python3 /app/src/geoapi.py

build: ## builds the docker image
	docker build . -t $(IMAGE_NAME) --build-arg uid=$(shell id -u) --build-arg gid=$(shell id -g) --build-arg user=dockeruser --build-arg group=dockergroup

shell:  ## enters a shell attached to the docker image just built
	docker run --user $(shell id -u):$(shell id -g) -v $(shell pwd):/app -w /app -it $(IMAGE_NAME) bash
