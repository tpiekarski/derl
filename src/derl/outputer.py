#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

from logging import getLogger
from derl.model.stats import get_stats

_logger = getLogger(__name__)
_stats = get_stats()


def output(files, stats=False):
    if len(files) == 0:
        _logger.debug("No matched files for output")
        return

    for file in files:
        print(file, end="")

    if stats:
        print(_stats)
