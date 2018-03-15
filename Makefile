VIRTUAL_ENV ?= venv
NODE_BIN = node_modules/.bin

install:
	npm install
	if [ ! -f $(VIRTUAL_ENV)/bin/python3 ]; then python3 -m venv $(VIRTUAL_ENV); fi
	$(VIRTUAL_ENV)/bin/python3 -m pip install -r requirements/dev.txt
	$(VIRTUAL_ENV)/bin/python3 manage.py migrate

makemessages:
	$(VIRTUAL_ENV)/bin/python manage.py makemessages -l de

server:
	$(VIRTUAL_ENV)/bin/python3 manage.py runserver 8007

.PHONY: lint-quick
lint-quick:
	. $(VIRTUAL_ENV)/bin/activate && $(NODE_BIN)/polylint -SF

.PHONY: release
release: export DJANGO_SETTINGS_MODULE ?= tempelhof.settings.build
release:
	npm install --silent
	npm run build
	$(VIRTUAL_ENV)/bin/python3 -m pip install -r requirements.txt -q
	$(VIRTUAL_ENV)/bin/python3 manage.py compilemessages -v0
	$(VIRTUAL_ENV)/bin/python3 manage.py collectstatic --noinput -v0

