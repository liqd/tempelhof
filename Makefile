VIRTUAL_ENV ?= .env
NODE_BIN = node_modules/.bin
SCSS_FILES := $(shell find 'tempelhof/assets/scss' -name '*.scss')
JS_FILES := $(shell find 'tempelhof/assets/js' | grep '\.jsx\?$$')
PO_FILES := $(shell find . -name '*.po')

install:
	npm install
	if [ ! -f $(VIRTUAL_ENV)/bin/python3 ]; then python3 -m venv $(VIRTUAL_ENV); fi
	$(VIRTUAL_ENV)/bin/python3 -m pip install -r requirements/dev.txt
	$(VIRTUAL_ENV)/bin/python3 manage.py migrate

webpack: $(SCSS_FILES) $(JS_FILES)
	$(NODE_BIN)/webpack

webpack-prod: $(SCSS_FILES) $(JS_FILES)
	$(NODE_BIN)/webpack --define process.env.NODE_ENV="'production'" --optimize-minimize --devtool none

makemessages:
	$(VIRTUAL_ENV)/bin/python manage.py makemessages -l de

compilemessages: $(PO_FILES)
	$(VIRTUAL_ENV)/bin/python manage.py compilemessages

build: webpack compilemessages

server:
	$(VIRTUAL_ENV)/bin/python3 manage.py runserver 8000
