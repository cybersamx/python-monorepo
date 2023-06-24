ROOT_DIR := $(shell git rev-parse --show-toplevel)
VENV := .venv
PYTHON := $(VENV)/bin/python3
PIP := $(VENV)/bin/pip
VIRTUAL_ENV := python3 -m venv

# Colorized print
BOLD := $(shell tput bold)
RED := $(shell tput setaf 1)
BLUE := $(shell tput setaf 4)
RESET := $(shell tput sgr0)

# Default target

.PHONY: all
all: run

##@ run: Install packages

.PHONY: install
install: venv
	@echo "$(BOLD)$(BLUE)Install packages $(VENV).$(RESET)"
	$(PIP) install -r $(ROOT_DIR)/requirements-pip.txt
	$(PIP) install -r $(ROOT_DIR)/requirements-tools.txt
	$(PIP) install -r requirements.txt
	@echo "$(BOLD)$(GREEN)Installed a virtual environment called $(VENV).$(RESET)"
	@echo "$(BOLD)$(BLUE)You don't need to activate venv if you are using make for this project.$(RESET)"
	@echo "$(BOLD)$(BLUE)If you want to activate the root venv, please run source $(VENV)/bin/activate.$(RESET)"

# If virtual environment has been set up, we won't see the activate file.
$(VENV)/bin/activate: ../../requirements-pip.txt ../../requirements-tools.txt
	@echo "$(BOLD)$(BLUE)Setting up virtual environment $(VENV).$(RESET)"
	$(VIRTUAL_ENV) $(VENV)

# Phony target for running the virtual environment setup
.PHONY: venv
venv: $(VENV)/bin/activate

##@ run: Run the program

.PHONY: run
run: venv lint
	@echo "$(BOLD)$(BLUE)Build the python project.$(RESET)"
	$(PYTHON) main.py

##@ lint: Run a linter against the project

.PHONY: lint
lint:
	@echo "$(BOLD)$(BLUE)Run linter against the python project.$(RESET)"
	flake8 --filename=*.py cyberlib_base

##@ test: Test unit tests

.PHONY: test
test: venv
	@echo "$(BOLD)$(BLUE)Run all unit tests.$(RESET)"
	python -m pytest tests

##@ clean: Clean output files and build cache

.PHONY: clean
clean:
	@echo "$(BOLD)$(RED)Removing build cache.$(RESET)"
	rm -rf __pycache__
	find . -type f -name '*.pyc' -delete

##@ help: Help

.PHONY: help
help: Makefile
	@-echo " Usage:\n  make $(BLUE)<target>$(RESET)"
	@-echo
	@-sed -n 's/^##@//p' $< | column -t -s ':' | sed -e 's/[^ ]*/ &/2'
