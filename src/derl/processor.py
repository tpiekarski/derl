# -*- coding: utf-8 -*-

import logging

from pathlib import Path

_logger = logging.getLogger(__name__)


def process_directory(directory):
    _logger.info("Starting to process directory '{}'".format(directory))

    files = []
    path = Path(directory)

    for p in path.iterdir():
        if (p.is_file()):
            files.append(p)

    _logger.info("Finished processing directory")
    _logger.info("Found {} files in '{}'".format(len(files), directory))
    _logger.debug(files)

    return files
