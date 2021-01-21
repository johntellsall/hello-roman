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

setup:
	python3 -m pip install --upgrade pip
	python3 -m pip install -r ./requirements.txt
	
lint:
	python3 -m flake8 $$(git ls-files '*.py')

test:
	python3 ./manage.py test -v2

# local:
# 	django-admin runserver --pythonpath=. --settings=tinyapp

cycle-tests:
	while true \
	; do tput bold ; date ; tput sgr0 \
	; ./manage.py test ; sleep 10 \
	; done
