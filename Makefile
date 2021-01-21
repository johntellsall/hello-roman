RUN := docker-compose run web 

all:

# list -- list all files in project
list:
	rg --files .

# up -- run project
up:
	docker-compose up

shell:
	docker-compose run web bash

lint:
	flake8 $$(git ls-files '*.py')

test:
	./manage.py test

# local:
# 	django-admin runserver --pythonpath=. --settings=tinyapp

cycle-tests:
	while true \
	; do tput bold ; date ; tput sgr0 \
	; ./manage.py test ; sleep 10 \
	; done
