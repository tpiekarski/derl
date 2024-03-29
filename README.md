# derl

[![Build Status](https://app.travis-ci.com/tpiekarski/derl.svg?branch=master)](https://app.travis-ci.com/github/tpiekarski/derl) [![Coverage Status](https://coveralls.io/repos/github/tpiekarski/derl/badge.svg?branch=feature/integrate-coveralls)](https://coveralls.io/github/tpiekarski/derl?branch=feature/integrate-coveralls) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=tpiekarski_derl&metric=alert_status)](https://sonarcloud.io/dashboard?id=tpiekarski_derl)

[Overview](#overview) / [Features](#features) / [Install](#install) / [Run](#run) / [Usage](#usage) /
[Development](#development) / [Structures](#structures) / [Links](#links)

*Command Line Interface (CLI) utility for searching **de**ad U**RL**s inside files*

## [Overview](#overview)

The CLI utility takes a directory, finds all files recursively and looks for valid URLs. For every
URL an HTTP GET request is sent. All returning HTTP Status Codes are gathered in a list which is
written to *stdout*, can be sorted, filtered and further processed with tools like sed, awk or grep.

## [Features](#features)

- Iterating over directories and gathering a list of all files.
- Search for valid [URLs](https://developer.mozilla.org/en-US/docs/Glossary/URL) (http and https)
  inside the files and store all found URLs
- Send an optional [HTTP GET](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET) request
  to all URLs with custom timeout and retry (soon multi-threaded)
- Record all returning [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- Output a list of files, urls and line numbers (optional with context up to 3 lines)
- Common verbosity by default arguments (```-v|-vv```) with additional output for information and debugging
- Collect statistics about processed directories, files, lines, URLs and sent requests
- Track running time for processing files, searching URLs and dispatching requests

- *Utilities name sounds like one guy hunting for other dead things in the 10th season already ;)*

### Limitations

- At the moment only [UTF-8](http://doc.cat-v.org/plan_9/4th_edition/papers/utf) is supported, 
  relative paths are saved and no binary files are processed.

## [Install](#install)

```sh
# Makefile targets without a Python Virtual Environment
make requirements install-user

# Or without makefile inside a Python Virtual Environment
python -m venv .venv_run
source .venv_run/bin/activate
pip install -r requirements.txt
python setup.py install --user --record files.log
deactivate
```

This installation will copy files to ```$HOME/.local/``` and create *files.log*. This log stores 
all installed files for convenience. To uninstall run the following:

```sh
# Makefile target
make uninstall

# Or without makefile something like this:
xargs rm -rvf < files.log && rm -fv files.log
```

## [Run](#run)

```sh
derl --dispatch directory
```

### Output

```sh
$ derl --dispatch tests/test-directory/

tests/test-directory/dir-1/dir-2/test-4-dir-2.txt:1, 200, http://www.python.org/
tests/test-directory/dir-1/dir-2/test-4-dir-2.txt:4, 404, http://docs.python.org/something

# [...]

$ derl --context --dispatch tests/test-directory/

tests/test-directory/dir-1/dir-2/test-4-dir-2.txt:1, 200, http://www.python.org/
  Sed condimentum efficitur orci, sed mollis tellus mollis a. Nullam http://www.python.org/
  tempus magna ac felis iaculis rhoncus. Ut in sodales lectus. Integer vestibulum malesuada

tests/test-directory/dir-1/dir-2/test-4-dir-2.txt:4, 404, http://docs.python.org/something
  ullamcorper. Integer quis ultricies odio. Fusce tincidunt a ligula id blandit. Integer
  dignissim blandit turpis ac maximus. Donec http://docs.python.org/something eget justo tempus,
  mauris.

# [...]

$ derl --stats --dispatch tests/test-directory/

# [...]
tests/test-directory/test-2-dir-0.txt:3, 404, http://www.dlqx.de/test

Finished checking URLs after 1.00 second(s).
Processed Directories/Files/Lines/Tokens/URLs: 3/7/42/491/7
Sent HTTP GET Requests: 7
```

## [Usage](#usage)

```txt
derl [-h] [-c] [-d] [-r RETRY] [-s] [-t TIMEOUT] [--version] [-v] [-vv] directory

Dead URL searching utility

positional arguments:
  directory                      directory for looking for dead URLs

optional arguments:
  -h, --help                     show this help message and exit
  -c, --context                  showing up to 3 lines of context
  -d, --dispatch                 dispatching HTTP requests for every found URL
  -r RETRY, --retry RETRY        set how often to retry a request (default is 3)
  -s, --stats                    track and print statistics at the end
  -t TIMEOUT, --timeout TIMEOUT  set timeout for requests in seconds (default is 10)
  --version                      show program's version number and exit
  -v, --verbose                  set loglevel to INFO
  -vv, --very-verbose            set loglevel to DEBUG
```

## [Development](#development)

### Requirements, Tests and Development

```sh
# Makefile targets
make requirements test develop

# Or without Makefile
python -m venv .venv_run
source .venv_run/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
python setup.py test
python setup.py develop
deactivate
```

### Linting

```sh
# Linting project
make lint

# Generating report
make report
```

## [Structures](#structures)

### Data structure

```txt
files: [
  {
    filename,
    urls: [
      (0): {
        url,
        status_code,
        line_number
        context: [
          "line above matched line"
          "line with found URL",
          "line below matched line"
        ]
      },
      (1): {
        url,
        status_code,
        line_number
        context: [
          "line above matched line"
          "line with found URL",
          "line below matched line"
        ]
      },

      ...

      (n): {
        url,
        status_code,
        line_number
        context: [
          "line above matched line"
          "line with found URL",
          "line below matched line"
        ]
      }
    ]
  }
]
```

### Test directory structure

```txt
test-directory/
├── dir-1
│   ├── dir-2
│   │   ├── test-4-dir-2.txt
│   │   └── test-6-dir-2.txt
│   ├── test-3-dir-1.txt
│   ├── test-5-dir-1
│   └── test-7-dir-1.txt
├── test-1-dir-0.txt
└── test-2-dir-0.txt
```

### Recreating reference output

```sh
# Makefile target
make update-references

# Or without Makefile
derl tests/test-directory/ > tests/references/output-without-context-without-dispatch.out && \
derl tests/test-directory/ --context > tests/references/output-with-context-without-dispatch.out && \
derl tests/test-directory/ -d > tests/references/output-without-context-with-dispatch.out && \
derl tests/test-directory/ --context --dispatch > tests/references/output-with-context-with-dispatch.out
```

## [Links](#links)

- Blog, eshlox, [VS Code - sort Python imports automatically](https://eshlox.net/2019/12/02/vscode-sort-python-imports-automatically)
- Digital Ocean, [How-To Use String Formatters in Python 3](https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3)
- Findwork, [Advanced usage of Python requests - timeouts, retries, hooks](https://findwork.dev/blog/advanced-usage-python-requests-timeouts-retries-hooks/)
- Geeks for geeks, [Testing Output to stdout](https://www.geeksforgeeks.org/python-testing-output-to-stdout/)
- GitHub, [Python Primer for Java Developers](https://lobster1234.github.io/2017/05/25/python-java-primer/)
- Medium, [Testing sys.exit() with pytest](https://medium.com/python-pandemonium/testing-sys-exit-with-pytest-10c6e5f7726f)
- Medium, [What the mock? — A cheatsheet for mocking in Python](https://medium.com/@yeraydiazdiaz/what-the-mock-cheatsheet-mocking-in-python-6a71db997832)
- Programiz, [Python Tuple](https://www.programiz.com/python-programming/tuple)
- Pylint Tutorial, [A Beginner’s Guide to Code Standards in Python](https://docs.pylint.org/en/1.6.0/tutorial.html)
- PyScaffold, [Installation](https://pyscaffold.org/en/latest/install.html) and [Examples](https://pyscaffold.org/en/latest/examples.html)
- Python How-To, [Sorting How-To](https://docs.python.org/3/howto/sorting.html)
- Python Reference, [argparse — Parser for command-line options, arguments and sub-commands](https://docs.python.org/3/library/argparse.html#action)
- Python Reference, [Basic customization to data models](https://docs.python.org/3/reference/datamodel.html#customization)
- Python Reference, [Mock Object Library](https://docs.python.org/3/library/unittest.mock.html)
- Python Reference, [pathlib — Object-oriented filesystem paths](https://docs.python.org/3/library/pathlib.html)
- Python Reference, [re - Regular expression operations](https://docs.python.org/3/library/re.html)
- Python Tips, [Enumerate](https://book.pythontips.com/en/latest/enumerate.html)
- Python Tutorial, [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- Python, [The Python Tutorial](https://docs.python.org/3.7/tutorial/index.html)
- Readthedocs, [Requests for humans, Quickstart](https://requests.readthedocs.io/en/master/user/quickstart/)
- Real Python, [Understanding the Python Mock Object Library](https://realpython.com/python-mock-library/#managing-a-mocks-side-effects)
- Stack Overflow [Python mock requests.post to throw exception](https://stackoverflow.com/questions/48723711/python-mock-requests-post-to-throw-exception)
- Stack Overflow, [Accessing the index in 'for' loops?](https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops)
- Stack Overflow, [Can I set max_retries for requests.request?](https://stackoverflow.com/questions/15431044/can-i-set-max-retries-for-requests-request)
- Stack Overflow, [Control formatting of the argparse help argument list?](https://stackoverflow.com/questions/5462873/control-formatting-of-the-argparse-help-argument-list)
- Stack Overflow, [Python __str__ and lists](https://stackoverflow.com/questions/727761/python-str-and-lists)
- Stack Overflow, [Remove all the lines before the first line that contains a match?](https://unix.stackexchange.com/questions/257082/remove-all-the-lines-before-the-first-line-that-contains-a-match)
- Stack Overflow, [Why does "return list.sort()" return None, not the list?](https://stackoverflow.com/questions/7301110/why-does-return-list-sort-return-none-not-the-list)
- Twilio, [HTTP Requests in Python 3](https://www.twilio.com/blog/2016/12/http-requests-in-python-3.html)
- Youtube, [Learn Python in 60 Minutes from Java](https://www.youtube.com/watch?v=xLovcfIugy8)
