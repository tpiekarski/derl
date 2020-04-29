# -*- coding: utf-8 -*-

import logging

from pathlib import Path

_logger = logging.getLogger(__name__)


def process_directory(directory):
    _logger.info("Starting to process directory '%s'", directory)

    files = []

    try:
        path = Path(directory)
        for current in path.iterdir():
            if current.is_file():
                files.append(current)

        _logger.info("Finished processing directory")
        _logger.info("Found %i files in '%s'", len(files), directory)
        _logger.debug(files)
    except FileNotFoundError:
        _logger.error("Cannot access '%s': No such directory", directory)

    return files
