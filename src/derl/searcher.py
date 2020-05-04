# -*- coding: utf-8 -*-

import logging
import re

_logger = logging.getLogger(__name__)
_pattern = re.compile("^(http|https):\/\/.*", re.IGNORECASE)


def search_urls(files):
    _logger.info("Starting to search for URLs in %i files...", len(files))

    if len(files) == 0:
        _logger.info("No files are available for searching.")
        return

    for current_entry in files:
        with open(current_entry, "r") as current_file:

            _logger.debug("Spliting file %s into lines...", current_file.name)
            lines = current_file.readlines()
            _logger.debug("Found %i lines", len(lines))

            for current_line in lines:
                _logger.debug("Splitting current line into tokens...")
                tokens = current_line.split()
                _logger.debug("Found %i tokens", len(tokens))

                for current_token in tokens:
                    match = _pattern.match(current_token)
                    if match:
                        _logger.info("Found a match (%s) in file '%s'", match.string, current_file.name)
