VIRTUAL_ENV ?= .env
NODE_BIN = node_modules/.bin
SCSS_FILES := $(shell find 'tempelhof/assets/scss' -name '*.scss')
JS_FILES := $(shell find 'tempelhof/assets/js' | grep '\.jsx\?$$')

install:
	npm install
	if [ ! -f $(VIRTUAL_ENV)/bin/python3 ]; then python3 -m venv $(VIRTUAL_ENV); fi
	$(VIRTUAL_ENV)/bin/python3 -m pip install -r requirements/dev.txt
	$(VIRTUAL_ENV)/bin/python3 manage.py migrate

webpack: $(SCSS_FILES) $(JS_FILES)
	$(NODE_BIN)/webpack

build: webpack

server:
	$(VIRTUAL_ENV)/bin/python3 manage.py runserver 8000
