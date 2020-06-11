# -*- coding: utf-8 -*-

import logging

from os import path

_logger = logging.getLogger(__name__)


def check_directory(directory):
    _logger.info("Checking provided directory %s", directory)

    return path.isdir(directory)
