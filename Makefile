# venv settings
export PROJECT_PATH := src
export PYTHONPATH   := $(PROJECT_PATH):tests/fixtures
export VIRTUALENV   := $(PWD)/.venv
export PATH         := $(VIRTUALENV)/bin:$(PATH)

# fix make <= 3.81 (macOS and old Linux distros)
ifeq ($(filter undefine,$(value .FEATURES)),)
SHELL = env PATH="$(PATH)" /bin/bash
endif

all:

.PHONY: .venv

.env:
	echo 'PYTHONPATH="$(PYTHONPATH)"' > .env

.venv:
	python3.12 -m venv $(VIRTUALENV)
	pip install --upgrade pip

install: .venv .env
	if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

activate:
	. $(VIRTUALENV)/bin/activate

ptnetinspector: install activate
# 	pip install ptnetinspector
	pip install -e .

interface: activate
	python3 interface-web/app.py

