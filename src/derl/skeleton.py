# -*- coding: utf-8 -*-

import argparse
import sys
import logging

from derl import __version__
from derl.processor import process_directory

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
        metavar="directory"
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
    _logger.debug("Checking provided directory {}".format(directory))

    # todo: check if directory exists and is readable

    return True


def main(args):
    args = parse_args(args)
    setup_logging(args.loglevel)

    if (not check_directory(args.directory)):
        _logger.error("Invalid directory provided, aborting.")
        sys.exit(-1)

    files = process_directory(args.directory)


def run():
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
