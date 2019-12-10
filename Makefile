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
	@echo 

.PHONY: style
style:
	yapf --style google --parallel -i $(SRCS)

.PHONY: lint
lint:
	pylint -v $(SRCS)
	
.PHONY:	test
#test:  check
#	${PYTHON} -m pytest

.PHONY:	run
run:
	${PYTHON} wordpuzzle.py

.PHONY:	clean
clean:
	@echo Please implement me!
	@echo delete all *.pyc
