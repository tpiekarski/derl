# -*- coding: utf-8 -*-

from unittest import TestCase

from derl.processor import process_directory

_TEST_DIRECTORY = "tests/test-directory"


class ProcessorTest(TestCase):

    def test_process_file(self):
        # todo: implement test
        print("NYI")

    def test_process_line(self):
        # todo: implement test
        print("NYI")

    def test_process_token(self):
        # todo: implement test
        print("NYI")

    def test_process_directory(self):
        self.assertEqual(len(process_directory(_TEST_DIRECTORY, [])), 4)
        self.assertEqual(len(process_directory("not-existing-directory", [])), 0)
