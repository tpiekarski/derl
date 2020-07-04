#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

from concurrent.futures import as_completed
from logging import getLogger

_DEFAULT_WORKER = 2
_logger = getLogger(__name__)


def _calc_max_work(items: int, worker: int) -> int:
    if items % worker == 0:
        max_items = int(items / worker)
    else:
        _logger.debug("Normalizing items (Modulo until geting even max_items")
        normalized_items = items

        while normalized_items % worker != 0:
            normalized_items = (normalized_items + (normalized_items % worker))

        max_items = int(normalized_items / worker)

    _logger.debug("Maximum work for %i items and %i worker should be %i.", items, worker, max_items)

    return max_items


def _prepare_distribution_list(worker: int) -> list:
    distributed_payload = []
    for _ in range(worker):
        distributed_payload.append(list())

    return distributed_payload


def _distribute(payload: list, worker: int) -> list:
    items = len(payload)
    max_items = _calc_max_work(items, worker)
    distributed_payload = _prepare_distribution_list(worker)
    queue = 0
    pos = 0

    _logger.debug("Distributing %i items to %i lists with %i items each.", items, worker, max_items)

    for current_item in range(items):
        if pos == max_items:
            queue += 1
            pos = 0

        distributed_payload[queue].append(payload[current_item])
        pos += 1

    return distributed_payload


def execute(executor, function: "function", payload: list, worker: int = _DEFAULT_WORKER) -> list:
    distributed_payload = _distribute(payload, worker)

    workers = []
    for submission in range(worker):
        _logger.info("Submitting work to worker...")
        workers.append(executor.submit(function, distributed_payload[submission]))

    results = []
    for current_worker in as_completed(workers):
        _logger.info("Collecting results from worker...")
        results += current_worker.result()

    _logger.info("Collected all results")

    return results
