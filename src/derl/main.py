#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#


import sys

from logging import basicConfig, getLogger

from derl.checker import check_arguments
from derl.collector import collect_context
from derl.dispatcher import request
from derl.executor import multi_process
from derl.filterer import filter_not_matching
from derl.outputer import output
from derl.parser import parse_args
from derl.processor import process_directory
from derl.searcher import search_urls
from derl.tracker import get_tracker

__author__ = "Thomas Piekarski"
__copyright__ = "Thomas Piekarski"
__license__ = "mit"

_logger = getLogger(__name__)
_tracker = get_tracker()


def setup_logging(loglevel: int):
    basicConfig(
        datefmt="%Y-%m-%d %H:%M:%S",
        format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s",
        level=loglevel,
        stream=sys.stdout
    )


def main(args: list):
    args = parse_args(args)
    setup_logging(args.loglevel)
    check_arguments(args)

    _tracker.start()
    processed_directories = process_directory(args.directory, [])
    # searched_files = search_urls(processed_directories)
    searched_files = multi_process(processed_directories, search_urls, 4)

    filtered_files = filter_not_matching(searched_files)

    if args.dispatch:
        filtered_files = request(filtered_files, args.timeout)

    if args.context:
        filtered_files = collect_context(filtered_files)

    _tracker.stop()
    output(filtered_files, args.stats)

    sys.exit(0)


def run():
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
