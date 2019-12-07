all:

# list -- list all files in project
list:
	rg --files .

# up -- run project
up:
	docker-compose up

