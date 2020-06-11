# -*- coding: utf-8 -*-

import logging

from os import path
from magic import from_file

_logger = logging.getLogger(__name__)


def is_text_file(file):
    _logger.debug("Checking file %s", file)
    mimetype = from_file(str(file), mime=True)

    return mimetype[:4] == "text"


def is_directory(value):
    _logger.debug("Checking provided directory %s", value)

    return path.isdir(value)
