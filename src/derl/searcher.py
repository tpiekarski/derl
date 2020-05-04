# -*- coding: utf-8 -*-

import logging

_logger = logging.getLogger(__name__)


def search_urls(files):
    _logger.info("Starting to search for URLs in %i files...", len(files))

    if len(files) == 0:
        _logger.info("No files are available for searching.")
        return

    for current_entry in files:
        with open(current_entry, "r") as current_file:
            lines = current_file.readlines()
            for current_line in lines:
                _logger.debug(current_line)

                # todo: implement searching for URLs
