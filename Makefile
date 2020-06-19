#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

SHELL:=/bin/bash
TEST_DIRECTORY=tests/test-directory/
LINT_JOBS=0 # auto-detect number of processors

.PHONY: build check clean develop lint run report requirements test update_references

build:
	$(info Building scripts)
	python setup.py build

check:
	$(info Checking package)
	python setup.py check

clean:
	$(info Cleaning build directories)
	python setup.py clean

commit: test lint

develop:
	$(info Install package in development mode)
	python setup.py develop --user

env:
	$(info Creating virtual environment in .venv)
	python -m venv .venv

install:
	$(info Installing package to users .local/)
	python setup.py install --record files.log

lint:
	$(info Linting source and test files)
	find src/ tests/ -name "*.py" | xargs pylint --rcfile=.pylintrc --jobs=$(LINT_JOBS) --output-format=colorized --verbose

report:
	$(info Genereting report with pylint and  removing lint results with sed)
	@find src/ tests/ -name "*.py" | \
		xargs pylint --jobs=$(LINT_JOBS) --reports=y --persistent=n --score=n --msg-template="" | \
		sed -e/Report/\{ -e:1 -en\;b1 -e\} -ed | less

requirements:
	$(info Installing requirements)
	pip install -r requirements.txt

run:
	$(info Testing if derl runs with $(TEST_DIRECTORY) (use args="" to pass arguments))
	derl $(TEST_DIRECTORY) $(args)

test:
	$(info Running functional and unit tests)
	python setup.py test

uninstall:
	$(info Uninstalling package)
	@test -f files.log \
		&& (xargs rm -rvf < files.log && rm -fv files.log) \
		|| echo "No files.log found in root directory, please run 'make install' again."

update-references:
	$(info Updating reference output)
	derl $(TEST_DIRECTORY) > tests/references/output-without-context-without-dispatch.out
	derl $(TEST_DIRECTORY) --context > tests/references/output-with-context-without-dispatch.out 
	derl $(TEST_DIRECTORY) -d > tests/references/output-without-context-with-dispatch.out
	derl $(TEST_DIRECTORY) --context --dispatch > tests/references/output-with-context-with-dispatch.out 
