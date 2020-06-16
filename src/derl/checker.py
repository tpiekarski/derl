#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

import sys

from logging import getLogger
from os import path
from magic import from_file

_INVALID_DIRECTORY = -1
_INVALID_TIMEOUT = -2
_INVALID_RETRY = -3

_logger = getLogger(__name__)


def is_directory(value):
    _logger.debug("Checking provided directory %s", value)

    return path.isdir(value)


def is_retry(value):
    return 0 < value <= 10


def is_text_file(file):
    _logger.debug("Checking file %s", file)
    mimetype = from_file(str(file), mime=True)

    return mimetype[:4] == "text"


def is_timeout(value):
    return value > 0


def check_arguments(args):
    if not is_timeout(args.timeout):
        _logger.error("Invalid timeout, timeout must be greater than 0")
        sys.exit(_INVALID_TIMEOUT)

    if not is_retry(args.retry):
        _logger.error("Invalid retry, retry must be greater than 0 and less or equal than 10")
        sys.exit(_INVALID_RETRY)

    if not is_directory(args.directory):
        _logger.error("Cannot access '%s': No such directory", args.directory)
        sys.exit(_INVALID_DIRECTORY)
