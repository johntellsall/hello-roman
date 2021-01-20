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

test:
	docker-compose run web ./manage.py test

# tiny:
# 	$(RUN) django-admin runserver --pythonpath=. --settings=tinyapp 0.0.0.0:8000

cycle-tests:
	while true \
	; do tput bold ; date ; tput sgr0 \
	; ./manage.py test ; sleep 10 \
	; done
