# Build static site for docs
docs:
	cd docs && make html

# This command will watch for new changes in doc files and rebuild it,
# but be aware that watchmedo can only look for changes in already
# existing files, not new
watch-docs:
	watchmedo shell-command --patterns="*.rst" --recursive --command="cd docs && make html"

.PHONY: lint
lint:
	pylint server

.PHONY: test
test:
	pytest

.PHONY: run
run:
	pipenv run django-admin runserver


install:
	npm i --production
	pipenv install

install-dev:
	npm i
	pipenv install --dev

build:
	npm run build

set-env:
	test -f .env && echo 'File .env already exists' || cp .env.default .env

# Fresh new installation
start: set-env install build run

start-dev: set-env install-dev build run

# Because I like to start server with one command =)
all: build
	django-admin runserver

# When dependencies are in alfabetical order it is so beautiful!
freeze:
	pip freeze | tr A-Z a-z | sort > requirements.txt
