#!/usr/bin/env make

# default goal if none requested
.DEFAULT: check

# globals
PYTHON	:= python3
SRCS	:= $(wildcard *.py **/*.py)

.PHONY: check
check:	style lint

.PHONY: help
help:
	@echo HELP
	@echo Start virtual env
	@echo load requirements
	@echo stop venv 

.PHONY: style
style:
	yapf --style google --parallel -i $(SRCS)

.PHONY: lint
lint:
	pylint -v $(SRCS)
	
.PHONY:	test
test:  check
	${PYTHON} -m pytest $(SRCS)

.PHONY:	run
run:
	${PYTHON} wordpuzzle.py

.PHONY:	clean
clean:
	$(RM) -rf cover
	$(RM) -rf .coverage
	$(RM) -rf __pycache__ wordpuzzle/__pycache__ tests/__pycache__ .pytest_cache/
	$(RM) -rf public
	$(RM) -rf python_*.egg-info/
	$(RM) -rf target
	$(RM) -v MANIFEST
	$(RM) -v *.pyc *.pyo *.py,cover
	$(RM) -v **/*.pyc **/*.pyo **/*.py,cover
