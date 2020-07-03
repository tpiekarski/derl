#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

from logging import getLogger

_logger = getLogger(__name__)


def filter_not_matching(files: list) -> list:
    filtered_files = []

    for current_file in files:
        if current_file.contains_urls():
            filtered_files.append(current_file)

    del files

    return filtered_files
