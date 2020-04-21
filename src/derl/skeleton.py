# -*- coding: utf-8 -*-

import argparse
import sys
import logging

from derl import __version__

__author__ = "Thomas Piekarski"
__copyright__ = "Thomas Piekarski"
__license__ = "mit"

_logger = logging.getLogger(__name__)


def parse_args(args):
    parser = argparse.ArgumentParser(description="Dead URL searching utility")
    parser.add_argument(
        action="store",  # default behavior
        dest="directory",
        help="directory for looking for dead URLs",
        metavar="directory",
        nargs=1
    )
    parser.add_argument(
        "--version",
        action="version",
        version="derl {ver}".format(ver=__version__)
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_const",
        const=logging.INFO,
        dest="loglevel",
        help="set loglevel to INFO",
    )
    parser.add_argument(
        "-vv",
        "--very-verbose",
        action="store_const",
        const=logging.DEBUG,
        dest="loglevel",
        help="set loglevel to DEBUG"
    )

    return parser.parse_args(args)


def setup_logging(loglevel):
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(
        datefmt="%Y-%m-%d %H:%M:%S",
        format=logformat,
        level=loglevel,
        stream=sys.stdout
    )


def check_directory(directory):
    _logger.info("Checking provided directory {}".format(directory))

    # todo: check if directory exists and is readable

    return True


def process_directory(directory):
    _logger.info("Starting to process directory {}".format(directory))

    files = []

    # todo: iterate and gather all files inside the directory

    return files


def main(args):
    args = parse_args(args)
    setup_logging(args.loglevel)

    # Example usage of the logger and its different levels
    # _logger.debug("Starting...")
    # _logger.info("Ending...")

    if (not check_directory(args.directory)):
        _logger.error("Invalid directory provided, aborting.")
        sys.exit(-1)

    files = process_directory(args.directory)


def run():
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
