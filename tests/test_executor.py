#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

from unittest import TestCase

from derl.executor import _distribute
from derl.model.file import File


def _generate_payload(amount: int) -> list:
    payload = []
    for current in range(amount):
        payload.append(File(str(current)))

    return payload


class ExecutorTest(TestCase):

    def test_even_distribution(self: "ExecutorTest"):
        payload = _generate_payload(6)
        distributed_payload = _distribute(payload, 2)

        self.assertEqual(len(distributed_payload), 2)
        self.assertEqual(len(distributed_payload[0]), 3)
        self.assertEqual(len(distributed_payload[1]), 3)

    def test_uneven1_distribution(self: "ExecutorTest"):
        payload = _generate_payload(7)
        distributed_payload = _distribute(payload, 2)

        self.assertEqual(len(distributed_payload), 2)
        self.assertEqual(len(distributed_payload[0]), 4)
        self.assertEqual(len(distributed_payload[1]), 3)

    def test_uneven2_distribution(self: "ExecutorTest"):
        payload = _generate_payload(13)
        distributed_payload = _distribute(payload, 2)

        self.assertEqual(len(distributed_payload), 2)
        self.assertEqual(len(distributed_payload[0]), 7)
        self.assertEqual(len(distributed_payload[1]), 6)

    def test_minimum_distribution(self: "ExecutorTest"):
        payload = _generate_payload(2)
        distributed_payload = _distribute(payload, 2)

        self.assertEqual(len(distributed_payload), 2)
        self.assertEqual(len(distributed_payload[0]), 1)
        self.assertEqual(len(distributed_payload[1]), 1)
