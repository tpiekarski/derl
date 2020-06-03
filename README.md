# derl

*A CLI utility for searching for **de**ad U**RL**s inside a project directory.*

## Test and Install

```sh
python setup.py test
python setup.py develop --user

derl tests/test-directory/
```

## Usage

```sh
usage: derl [-h] [--version] [-v] [-vv] directory

Dead URL searching utility

positional arguments:
  directory            directory for looking for dead URLs

optional arguments:
  -h, --help           show this help message and exit
  --version            show program's version number and exit
  -v, --verbose        set loglevel to INFO
  -vv, --very-verbose  set loglevel to DEBUG
```

## Concept

### Description

The CLI utility should take a directory as one argument, find all files recursively,
find all URLs inside those files and send an HTTP GET request. All returning codes
should be collected and then filtered by 404 Not found. The final list should be
output in a formatted way.

### Features

- Passing a command line argument with the directory to process
- Iterate over all subdirectories and gather a list of all files
  (Including relative path and skipping any binary files)
- Search for URLs (http and https) inside the file list and store all found URLs
- Send an HTTP GET request to all URLs (In later version this definitely should happen parallel)
- Record the returning HTTP Status Code
- Output a list of files and urls where a 404 was returned (something like file:line-number:url)

### Data structure

```txt
files: [
  {
    filename,
    relative path,
    urls: [
      (0): {
        url,
        response,
        line_number
      },
      (1): {
        url,
        response,
        line_number
      },

      ...

      (n): {
        url,
        response,
        line_number
      }
    ]
  }
]
```

## Test directory structure

```txt
test-directory/
├── dir-1
│   ├── dir-2
│   │   └── test-4-dir-2.txt
│   └── test-3-dir-1.txt
├── test-1-dir-0.txt
└── test-2-dir-0.txt

2 directories, 4 files
```

## References

- [A Beginner’s Guide to Code Standards in Python - Pylint Tutorial](https://docs.pylint.org/en/1.6.0/tutorial.html)
- [Basic customization to data models](https://docs.python.org/3/reference/datamodel.html#customization)
- [How To Use String Formatters in Python 3](https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3)
- [HTTP Requests in Python 3](https://www.twilio.com/blog/2016/12/http-requests-in-python-3.html)
- [Learn Python in 60 Minutes from Java](https://www.youtube.com/watch?v=xLovcfIugy8)
- [pathlib — Object-oriented filesystem paths](https://docs.python.org/3/library/pathlib.html)
- [PyScaffold](https://pyscaffold.org/)
- [Python Primer for Java Developers](https://lobster1234.github.io/2017/05/25/python-java-primer/)
- [re - Regular expression operations¶](https://docs.python.org/3/library/re.html)
- [Requests for humans, Quickstart](https://requests.readthedocs.io/en/master/user/quickstart/)
- [Testing Output to stdout](https://www.geeksforgeeks.org/python-testing-output-to-stdout/)
- [The Python Tutorial](https://docs.python.org/3.7/tutorial/index.html)
