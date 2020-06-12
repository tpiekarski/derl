#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

import logging

_logger = logging.getLogger(__name__)


def output(files):
    if len(files) == 0:
        _logger.debug("No matched files for output")
        return

    for file in files:
        print(file)
