# -*- coding: utf-8 -*-

import logging

from derl.processor import process_file

_logger = logging.getLogger(__name__)

_DEFAULT_ENCODING = "utf-8"


def search_urls(files):
    _logger.info("Starting to search for URLs in %i files...", len(files))

    if len(files) == 0:
        _logger.info("No files found, skipping search")
        return []

    for current_entry in files:
        with open(current_entry.filename, "r", encoding=_DEFAULT_ENCODING) as current_file:
            current_entry.urls = process_file(current_file)

    _logger.debug("Searched %i files", len(files))

    return files
