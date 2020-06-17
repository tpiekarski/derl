#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

SHELL:=/bin/bash
TEST_DIRECTORY=tests/test-directory/

.PHONY: develop run test lint update_references

commit: test lint

check:
	$(info Checking package)
	python setup.py check

develop:
	$(info Install package in development mode)
	python setup.py develop --user

lint:
	$(info Linting source and test files)
	pylint src/derl/*.py && pylint tests/*.py

requirements:
	$(info Installing requirements)
	pip install -r requirements.txt

run:
	$(info Testing if derl runs with $(TEST_DIRECTORY) (use args="" to pass arguments))
	derl $(TEST_DIRECTORY) $(args)

test:
	$(info Running functional and unit tests)
	python setup.py test

update-references:
	$(info Updating reference output)
	derl $(TEST_DIRECTORY) > tests/references/output-without-context-without-dispatch.out
	derl $(TEST_DIRECTORY) --context > tests/references/output-with-context-without-dispatch.out 
	derl $(TEST_DIRECTORY) -d > tests/references/output-without-context-with-dispatch.out
	derl $(TEST_DIRECTORY) --context --dispatch > tests/references/output-with-context-with-dispatch.out 
