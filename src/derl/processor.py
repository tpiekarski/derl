# -*- coding: utf-8 -*-

import logging
import re

from pathlib import Path

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


def process_directory(directory, files=[]):
    _logger.info("Starting to process directory '%s'", directory)

    try:
        path = Path(directory)
        for current in path.iterdir():
            if current.is_file():
                _logger.debug("Appending file '%s'", current.name)
                files.append(current)
            elif current.is_dir():
                _logger.debug("'%s' is a directory, descending...", current.name)
                files = process_directory(current, files)
            else:
                _logger.debug("Skipping not regular file or directory")
                continue

        _logger.info("Finished processing directory '%s'", directory)
        _logger.info("Found %i files in '%s'", len(files), directory)
        _logger.debug(files)
    except FileNotFoundError:
        _logger.error("Cannot access '%s': No such directory", directory)

    return files
