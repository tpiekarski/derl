#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

from logging import getLogger
from derl.tracker import get_tracker

_logger = getLogger(__name__)
_tracker = get_tracker()


def output(files, stats=False):
    if len(files) == 0:
        _logger.debug("No matched files for output")
        return

    for file in files:
        print(file, end="")

    if stats:
        print(_tracker)
