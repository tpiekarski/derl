#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

from logging import getLogger
from os import path
from magic import from_file


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
