#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

from logging import getLogger

from derl.processor import process_file

_logger = getLogger(__name__)

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
