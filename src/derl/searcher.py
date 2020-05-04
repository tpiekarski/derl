# -*- coding: utf-8 -*-

import logging

from derl.processor import process_file

_logger = logging.getLogger(__name__)


def search_urls(files):
    _logger.info("Starting to search for URLs in %i files...", len(files))

    if len(files) == 0:
        _logger.info("No files found, skipping search")
        return

    for current_entry in files:
        with open(current_entry, "r") as current_file:
            process_file(current_file)
