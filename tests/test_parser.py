# -*- coding: utf-8 -*-

from unittest import TestCase

from derl.parser import parse_args


class ParserTest(TestCase):

    def test_parse_directory(self):
        parsed_args = parse_args(["test-directory"])

        self.assertEqual(parsed_args.directory, "test-directory")

    def test_parse_dispatch(self):
        self.assertTrue(parse_args(["test-directory", "-d"]).dispatch)
        self.assertTrue(parse_args(["test-directory", "--dispatch"]).dispatch)
        self.assertFalse(parse_args(["test-directory"]).dispatch)
