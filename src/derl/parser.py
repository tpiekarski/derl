# -*- coding: utf-8 -*-

import argparse
import logging

from derl import __version__


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
