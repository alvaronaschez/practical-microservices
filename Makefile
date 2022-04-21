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

db-up:
	docker volume create practical-microservices-pgdata
	docker run -d \
	 --name practical-microservices-db \
	 -e POSTGRES_USER=postgres \
	 -e POSTGRES_PASSWORD=mysecretpassword \
	 -e POSTGRES_DB=postgres \
	 -e PGDATA=/var/lib/postgresql/data \
	 -p 5432:5432 \
	 -v pgdata:/var/lib/postgresql/data \
	 postgres:14