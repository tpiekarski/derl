#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

from logging import getLogger
from pathlib import Path
from re import compile as rcompile, IGNORECASE
from typing import TextIO

from derl.checker import is_text_file, is_url
from derl.model.file import File
from derl.model.url import URL
from derl.tracker import get_tracker

_STARTING_LINE_NUMBER = 1

_logger = getLogger(__name__)
_pattern = rcompile(r"^(http|https):\/\/.*$", IGNORECASE)
_tracker = get_tracker()


def process_file(file: TextIO) -> list:
    _logger.debug("Splitting current file %s into lines...", file.name)
    _tracker.stats.inc_files()

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


def process_line(file: TextIO, line: tuple, urls: list) -> list:
    _logger.debug("Splitting current line into tokens...")
    _tracker.stats.inc_lines()

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


def process_token(file: TextIO, token: str, line_number: int) -> URL:
    _tracker.stats.inc_tokens()

    match = _pattern.match(token)
    url = None

    if match and is_url(match.string):
        _logger.info("Found a match (%s) in file '%s'", match.string, file.name)
        _tracker.stats.inc_urls()
        url = URL(match.string, line_number)

    return url


def process_directory(directory: str, files: list) -> list:
    _logger.info("Starting to process directory '%s'", directory)
    _tracker.stats.inc_directories()

    try:
        path = Path(directory)
        for current in path.iterdir():
            if current.is_dir():
                _logger.debug("'%s' is a directory, descending...", current.name)
                files = process_directory(str(current), files)
            elif is_text_file(current):
                _logger.debug("Appending file '%s'", current.name)
                files.append(File(current))
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
