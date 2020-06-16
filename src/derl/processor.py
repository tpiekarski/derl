#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

from logging import getLogger
from pathlib import Path
from re import compile as rcompile, IGNORECASE

from derl.checker import is_text_file
from derl.model.file import File
from derl.model.url import URL


_STARTING_LINE_NUMBER = 1

_logger = getLogger(__name__)
_pattern = rcompile(r"^(http|https):\/\/.*$", IGNORECASE)


def process_file(file):
    _logger.debug("Spliting current file %s into lines...", file.name)

    try:
        lines = list(enumerate(file.readlines(), _STARTING_LINE_NUMBER))
    except UnicodeDecodeError:
        _logger.error("Failed to read line of file %s, skipping file", file.name)
        return []

    urls = []

    if len(lines) == 0:
        _logger.debug("No lines found, skipping file '%s'", file.name)
        return urls

    _logger.debug("Found %i lines", len(lines))

    for current_line in lines:
        process_line(file, current_line, urls)

    return urls


def process_line(file, line, urls):
    _logger.debug("Splitting current line into tokens...")
    line_number, line_content = line
    tokens = line_content.split()

    if len(tokens) == 0:
        _logger.debug("No tokens found, skipping line")
        return urls

    _logger.debug("Found %i tokens", len(tokens))

    for current_token in tokens:
        url = process_token(file, current_token, line_number)

        if url is not None:
            urls.append(url)

    return urls


def process_token(file, token, line_number):
    match = _pattern.match(token)
    url = None

    if match:
        _logger.info("Found a match (%s) in file '%s'", match.string, file.name)
        url = URL(match.string, line_number)

    return url


def process_directory(directory, files):
    _logger.info("Starting to process directory '%s'", directory)

    try:
        path = Path(directory)
        for current in path.iterdir():
            if current.is_file() and is_text_file(str(current)):
                _logger.debug("Appending file '%s'", current.name)
                files.append(File(current))
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

    files.sort(key=lambda file: file.filename)

    return files
