SHELL := /bin/zsh

PYTHON = env/bin/python
PIP = env/bin/pip

test:
	echo "TODO"
	echo "test"

install:
	$(PIP) install -r requirements.txt

repl:
	$(PYTHON)

run:
	source env/bin/activate
	cd src
	sanic src.server.app
