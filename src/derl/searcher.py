# -*- coding: utf-8 -*-

import logging
import re

_logger = logging.getLogger(__name__)
_pattern = re.compile(r"^(http|https):\/\/.*$", re.IGNORECASE)


def process_file(file):
    _logger.debug("Spliting current file %s into lines...", file.name)
    lines = file.readlines()

    if len(lines) == 0:
        _logger.debug("No lines found, skipping file '%s'", file.name)
        return

    _logger.debug("Found %i lines", len(lines))

    for current_line in lines:
        process_line(file, current_line)


def process_line(file, line):
    _logger.debug("Splitting current line into tokens...")
    tokens = line.split()

    if len(tokens) == 0:
        _logger.debug("No tokens found, skipping line")
        return

    _logger.debug("Found %i tokens", len(tokens))

    for current_token in tokens:
        process_token(file, current_token)


def process_token(file, token):
    match = _pattern.match(token)

    if match:
        _logger.info("Found a match (%s) in file '%s'", match.string, file.name)


def search_urls(files):
    _logger.info("Starting to search for URLs in %i files...", len(files))

    if len(files) == 0:
        _logger.info("No files found, skipping search")
        return

    for current_entry in files:
        with open(current_entry, "r") as current_file:
            process_file(current_file)
