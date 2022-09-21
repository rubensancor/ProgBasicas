SHELL := /bin/bash

.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# .PHONY: clean
# clean: ## Cleans
# 	find ./app -type d -name __pycache__ -exec rm -r {} \+

.PHONY: down
down: ## Stops all containers and removes volumes
	docker-compose down --remove-orphans
	docker network rm traefik-public || true

#######################
## BUILD IMAGES
#######################

.PHONY: build
build: ## Buidls the images
	docker-compose build

#######################
## RUN CONTAINERS
#######################

.PHONY: up
up: down ## Starts containers
	docker network create traefik-public || true
	docker-compose up -d