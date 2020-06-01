# -*- coding: utf-8 -*-

from unittest import TestCase
from unittest.mock import patch
from io import StringIO

from derl.skeleton import check_directory, main, process_directory, parse_args

__author__ = "Thomas Piekarski"
__copyright__ = "Thomas Piekarski"
__license__ = "mit"

_TEST_DIRECTORY = "tests/test-directory"


class SkeletonTest(TestCase):

    def test_parse_arguments(self):
        raw_args = [_TEST_DIRECTORY]
        parsed_args = parse_args(raw_args)

        self.assertEqual(parsed_args.directory, _TEST_DIRECTORY)

    def test_check_directory(self):
        self.assertTrue(check_directory(_TEST_DIRECTORY))
        self.assertFalse(check_directory("not-existing-directory"))

    def test_process_directory(self):
        self.assertEqual(len(process_directory(_TEST_DIRECTORY, [])), 4)
        self.assertEqual(len(process_directory("not-existing-directory", [])), 0)

    def test_main(self):
        with patch("sys.stdout", new=StringIO()) as fake_stdout:
            with open("tests/reference-output.out", "r") as reference:
                main([_TEST_DIRECTORY])
                self.assertEqual(fake_stdout.getvalue(), reference.read())
