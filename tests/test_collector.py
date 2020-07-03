#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

from unittest import TestCase

from derl.collector import collect_context
from derl.model.file import File


def _build_test_files(filename: str, line_number: int) -> list:
    file = File(filename)
    file.append("http://www.python", line_number)
    files = [file]

    return files


class CollectorTest(TestCase):

    def test_collect_context(self: "CollectorTest"):
        files_with_context = collect_context(_build_test_files("tests/test-files/context.txt", 2))
        self.assertEqual(len(files_with_context[0].urls[0].context), 3)

    def test_collect_context_at_top_line(self: "CollectorTest"):
        files_with_context = collect_context(_build_test_files("tests/test-files/context-at-top.txt", 1))
        self.assertEqual(len(files_with_context[0].urls[0].context), 2)

    def test_collect_context_at_bottom_line(self: "CollectorTest"):
        files_with_context = collect_context(_build_test_files("tests/test-files/context-at-bottom.txt", 3))
        self.assertEqual(len(files_with_context[0].urls[0].context), 2)
