#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

import logging

from os import path
from magic import from_file

_logger = logging.getLogger(__name__)


def is_directory(value):
    _logger.debug("Checking provided directory %s", value)

    return path.isdir(value)


def is_text_file(file):
    _logger.debug("Checking file %s", file)
    mimetype = from_file(str(file), mime=True)

    return mimetype[:4] == "text"
