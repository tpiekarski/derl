#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

from unittest import TestCase

from conftest import _TEST_DIRECTORY
from derl.processor import process_directory, process_file, process_line


class ProcessorTest(TestCase):

    def test_process_empty_line(self: "ProcessorTest"):
        urls = []

        self.assertEqual(process_line(None, [0, ""], urls), [])

    def test_process_directory(self: "ProcessorTest"):
        self.assertEqual(len(process_directory(_TEST_DIRECTORY, [])), 7)
        self.assertEqual(len(process_directory("not-existing-directory", [])), 0)

    def test_unsupported_file_encoding(self: "ProcessorTest"):
        with open("tests/test-files/binary-data", "r") as test_file:
            self.assertEqual(process_file(test_file), [])

    def test_process_file_with_empty_lines(self: "ProcessorTest"):
        with open("tests/test-files/empty-file", "r") as test_file:
            self.assertEqual(process_file(test_file), [])
