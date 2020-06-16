#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#


import sys

from logging import basicConfig, getLogger

from derl.checker import is_directory, is_timeout
from derl.dispatcher import request
from derl.filterer import filter_not_matching
from derl.outputer import output
from derl.parser import parse_args
from derl.processor import process_directory
from derl.searcher import search_urls

__author__ = "Thomas Piekarski"
__copyright__ = "Thomas Piekarski"
__license__ = "mit"

_logger = getLogger(__name__)

_INVALID_DIRECTORY = -1
_INVALID_TIMEOUT = -2


def setup_logging(loglevel):
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    basicConfig(
        datefmt="%Y-%m-%d %H:%M:%S",
        format=logformat,
        level=loglevel,
        stream=sys.stdout
    )


def main(args):
    args = parse_args(args)
    setup_logging(args.loglevel)

    if not is_directory(args.directory):
        _logger.error("Cannot access '%s': No such directory", args.directory)
        sys.exit(_INVALID_DIRECTORY)

    if not is_timeout(args.timeout):
        _logger.error("Invalid timeout, timeout must be greater than 0")
        sys.exit(_INVALID_TIMEOUT)

    processed_directories = process_directory(args.directory, [])
    searched_files = search_urls(processed_directories)
    filtered_files = filter_not_matching(searched_files)

    if args.dispatch:
        output(request(filtered_files, args.timeout))
    else:
        output(filtered_files)

    sys.exit(0)


def run():
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
