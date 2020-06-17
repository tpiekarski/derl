#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

from argparse import ArgumentParser
from logging import DEBUG, INFO

from derl import __version__
from derl.dispatcher import _DEFAULT_RETRY, _DEFAULT_TIMEOUT


def parse_args(args):
    parser = ArgumentParser(description="Dead URL searching utility")
    parser.add_argument(
        action="store",  # default behavior
        dest="directory",
        help="directory for looking for dead URLs",
        metavar="directory")
    parser.add_argument(
        "-c",
        "--context",
        action="store_true",
        dest="context",
        help="showing up to 3 lines of context")
    parser.add_argument(
        "-d",
        "--dispatch",
        action="store_true",
        dest="dispatch",
        help="dispatching HTTP requests for every found URL")
    parser.add_argument(
        "-r",
        "--retry",
        action="store",
        default=_DEFAULT_RETRY,
        dest="retry",
        help="set how often to retry a request (default is 3)",
        type=int)
    parser.add_argument(
        "-t",
        "--timeout",
        action="store",
        default=_DEFAULT_TIMEOUT,
        dest="timeout",
        help="set timeout for requests in seconds (default is 10)",
        type=int)
    parser.add_argument(
        "--version",
        action="version",
        version="derl {ver}".format(ver=__version__))
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_const",
        const=INFO,
        dest="loglevel",
        help="set loglevel to INFO",)
    parser.add_argument(
        "-vv",
        "--very-verbose",
        action="store_const",
        const=DEBUG,
        dest="loglevel",
        help="set loglevel to DEBUG")

    return parser.parse_args(args)
