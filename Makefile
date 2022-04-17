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
	$(PYTHON) src/server.py
