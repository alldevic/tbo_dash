#!/usr/bin/make

include .env

SHELL = /bin/sh
CURRENT_UID := $(shell id -u):$(shell id -g)

export CURRENT_UID

ifeq ($(DEBUG), True)
	IMAGES := backend-dev postgres
	BACKEND_CONTAINER = tbo_backend_dev
else
	IMAGES := backend postgres
	BACKEND_CONTAINER = tbo_backend
endif

export IMAGES
export BACKEND_CONTAINER

up:
	DEBUGPY=False docker-compose up -d --force-recreate --build --remove-orphans $(IMAGES)
upd:
	DEBUGPY=True docker-compose up -d  --build $(IMAGES)
down:
	DEBUGPY=True docker-compose down
sh:
	docker exec -it /$(BACKEND_CONTAINER) /bin/sh
migrations:
	docker exec -it /$(BACKEND_CONTAINER) python3 manage.py makemigrations
su:
	docker exec -it /$(BACKEND_CONTAINER) python3 manage.py createsuperuser
logs:
	docker logs /$(BACKEND_CONTAINER) -f
volumes:
	docker volume create tbo_db_data
