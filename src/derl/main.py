#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#


import sys

from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from logging import basicConfig, getLogger
from os import cpu_count

from derl.checker import check_arguments
from derl.collector import collect_context
from derl.dispatcher import request
from derl.executor import execute
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

    max_process = cpu_count()

    _tracker.start()
    processed_directories = process_directory(args.directory, [])

    with ProcessPoolExecutor() as process_executor:
        searched_files = execute(process_executor, search_urls, processed_directories, max_process)
        filtered_files = filter_not_matching(searched_files)

        if args.context:
            filtered_files = execute(process_executor, collect_context, filtered_files, max_process)

    if args.dispatch:
        with ThreadPoolExecutor() as thread_executor:
            max_threads = max_process * 4
            filtered_files = execute(thread_executor, request, filtered_files, max_threads)

    _tracker.stop()
    output(filtered_files, args.stats)

    sys.exit(0)


def run():
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
