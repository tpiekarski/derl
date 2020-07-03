#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

SHELL:=/bin/bash
REFERENCE_DIRECTORY=tests/references
TEST_DIRECTORY=tests/test-directory
LINT_JOBS=0 # auto-detect number of processors

.PHONY: build check clean commit test lint develop env install install-user lint report requirements \
	requirements-dev run test uninstall update-references

build:
	$(info Building scripts)
	python setup.py build

clean:
	$(info Cleaning build directories)
	python setup.py clean

develop:
	$(info Install package in development mode)
	python setup.py develop --user

env:
	$(info Creating virtual environment in .venv)
	python -m venv .venv

install:
	$(info Installing package)
	python setup.py install --record files.log

install-user:
	$(info Installing package to users .local/)
	python setup.py install --user --record files.log

lint:
	$(info Linting source and test files)
	find src/ tests/ -name "*.py" | xargs pylint --rcfile=.pylintrc --jobs=$(LINT_JOBS) --output-format=colorized --verbose

pre-commit: run test lint

report:
	$(info Genereting report with pylint and removing lint results with sed)
	@find src/ tests/ -name "*.py" | \
		xargs pylint --jobs=$(LINT_JOBS) --reports=y --persistent=n --score=n --msg-template="" | \
		sed -e/Report/\{ -e:1 -en\;b1 -e\} -ed | less

requirements:
	$(info Installing requirements)
	pip install -r requirements.txt

requirements-dev:
	$(info Installing development requirements)
	pip install -r requirements-dev.txt

run:
	$(info Testing if derl runs with $(TEST_DIRECTORY) (use args="" to pass arguments))
	derl $(TEST_DIRECTORY) $(args)

show-function-signatures:
	$(info Showing all function (and method) signatures)
	find src/ tests/ -name "*.py" | xargs grep -E "def.*\(.*\).*:"

sonar:
	$(info Running Sonar Scanner (only when automatic analysis is turned off))
	sonar-scanner -Dsonar.login=${SONAR_KEY}

test:
	$(info Running functional and unit tests)
	python setup.py test

uninstall:
	$(info Uninstalling package)
	@test -f files.log \
		&& (xargs rm -rvf < files.log && rm -fv files.log) \
		|| echo "No files.log found in root directory, please run 'make install' again."

update-references:
	$(info Updating reference output in 'tests/references')
	derl $(TEST_DIRECTORY) > $(REFERENCE_DIRECTORY)/output-without-context-without-dispatch.out
	derl $(TEST_DIRECTORY) --context > $(REFERENCE_DIRECTORY)/output-with-context-without-dispatch.out 
	derl $(TEST_DIRECTORY) --dispatch > $(REFERENCE_DIRECTORY)/output-without-context-with-dispatch.out
	derl $(TEST_DIRECTORY) --context --dispatch > $(REFERENCE_DIRECTORY)/output-with-context-with-dispatch.out 
	derl $(TEST_DIRECTORY) --stats > $(REFERENCE_DIRECTORY)/output-with-stats-without-dispatch.out
	derl $(TEST_DIRECTORY) --stats --dispatch > $(REFERENCE_DIRECTORY)/output-with-stats-with-dispatch.out
