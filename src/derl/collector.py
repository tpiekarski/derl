#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

from logging import getLogger

from derl.model.url import URL

_logger = getLogger(__name__)

_DEFAULT_ENCODING = "utf-8"


def _extract_context(url: URL, lines: list) -> list:
    _logger.debug("Extracting context for the URL %s at line number %i", url.location, url.line_number)
    context = []
    line_index = url.line_number - 1

    if line_index - 1 >= 0:
        context.append(lines[line_index - 1])

    context.append(lines[line_index])

    if line_index + 1 < len(lines):
        context.append(lines[line_index + 1])

    return context


def collect_context(files: list) -> list:
    _logger.debug("Collecting context")
    for current_file in files:
        _logger.debug("Collecting context for file %s", current_file.filename)
        for current_url in current_file.urls:
            with open(current_file.filename, "r", encoding=_DEFAULT_ENCODING) as open_file:
                lines = open_file.readlines()
                context = _extract_context(current_url, lines)
                current_url.set_context(context)

    return files
