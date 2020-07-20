#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

import sys
from argparse import Namespace
from logging import getLogger
from os import path

from magic import from_file
from validators import url

_INVALID_DIRECTORY = -1
_INVALID_TIMEOUT = -2
_INVALID_RETRY = -3

_logger = getLogger(__name__)


def _is_directory(value: str) -> bool:
    _logger.debug("Checking provided directory %s", value)

    return path.isdir(value)


def _is_retry_value(value: int) -> bool:
    _logger.debug("Checking provided retry value %i", value)
    return 0 < value <= 10


def _is_timeout_value(value: int) -> bool:
    _logger.debug("Checking provided timeout value %i", value)
    return value > 0


def is_text_file(file: str) -> bool:
    _logger.debug("Checking provided file %s", file)
    mimetype = from_file(str(file), mime=True)

    return file.is_file() and mimetype[:4] == "text"


def is_valid_url(value: str) -> bool:
    _logger.debug("Checking provided URL %s", value)
    return url(value)


def check_arguments(args: Namespace):
    if not _is_timeout_value(args.timeout):
        _logger.error("Invalid timeout, timeout must be greater than 0")
        sys.exit(_INVALID_TIMEOUT)

    if not _is_retry_value(args.retry):
        _logger.error("Invalid retry, retry must be greater than 0 and less or equal than 10")
        sys.exit(_INVALID_RETRY)

    if not _is_directory(args.directory):
        _logger.error("Cannot access '%s': No such directory", args.directory)
        sys.exit(_INVALID_DIRECTORY)
