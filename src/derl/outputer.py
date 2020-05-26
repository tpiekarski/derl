# -*- coding: utf-8 -*-

import logging

_logger = logging.getLogger(__name__)


def output(files):
    if len(files) == 0:
        _logger.debug("No matched files for output")
        return

    for file in files:
        print(file)
