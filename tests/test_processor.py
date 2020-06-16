#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

from unittest import TestCase

from conftest import _TEST_DIRECTORY
from derl.processor import process_directory, process_line


class ProcessorTest(TestCase):

    def test_process_empty_line(self):
        urls = []

        self.assertEqual(process_line(None, [0, ""], urls), [])

    def test_process_directory(self):
        self.assertEqual(len(process_directory(_TEST_DIRECTORY, [])), 6)
        self.assertEqual(len(process_directory("not-existing-directory", [])), 0)
