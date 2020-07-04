#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

import concurrent.futures

_DEFAULT_WORKER = 2


def _calc_max_work(items: int, worker: int) -> int:
    if items % worker == 0:
        max_work = items / worker
    else:
        normalized_items = items

        while normalized_items % worker != 0:
            normalized_items = (normalized_items + (normalized_items % worker))

        max_work = normalized_items / worker

    return int(max_work)


def _prepare_distribution_list(worker: int) -> list:
    distributed_payload = []
    for _ in range(worker):
        distributed_payload.append(list())

    return distributed_payload


def _distribute(payload: list, worker: int) -> list:
    items = len(payload)
    max_work = _calc_max_work(items, worker)
    distributed_payload = _prepare_distribution_list(worker)
    queue = 0
    pos = 0

    for current_item in range(items):
        if pos == max_work:
            queue += 1
            pos = 0

        distributed_payload[queue].append(payload[current_item])
        pos += 1

    # todo: rethink that conditional one more time
    if max_work * worker < items:
        distributed_payload[worker - 1].append(payload[-1])

    return distributed_payload


def multi_process(payload: list, function: "function", worker: int = _DEFAULT_WORKER) -> list:
    with concurrent.futures.ProcessPoolExecutor() as executor:
        distributed_payload = _distribute(payload, worker)

        jobs = []
        for current_job in range(worker):
            jobs.append(executor.submit(function, distributed_payload[current_job]))

        results = []
        for current_job in concurrent.futures.as_completed(jobs):
            results += current_job.result()

        return results
