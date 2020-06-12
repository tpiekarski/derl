#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

import logging

_logger = logging.getLogger(__name__)


def filter_not_matching(files):
    filtered_files = []

    for current_file in files:
        if current_file.contains_urls():
            filtered_files.append(current_file)

    return filtered_files
