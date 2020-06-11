# -*- coding: utf-8 -*-

from unittest import TestCase
from unittest.mock import patch
from io import StringIO

from derl.main import check_directory, main, process_directory, parse_args

_TEST_DIRECTORY = "tests/test-directory"


class MainTest(TestCase):

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

    def _reference_testing(self, arguments, reference):
        with patch("sys.stdout", new=StringIO()) as fake_stdout:
            with open(reference, "r") as opened_reference:
                main(arguments)
                self.assertEqual(fake_stdout.getvalue(), opened_reference.read())

    def test_main_without_dispatch(self):
        self._reference_testing([_TEST_DIRECTORY], "tests/references/output-without-dispatch.out")

    def test_main_with_dispatch(self):
        self._reference_testing(["--dispatch", _TEST_DIRECTORY], "tests/references/output-with-dispatch.out")
