#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

from unittest import TestCase

from derl.parser import parse_args


class ParserTest(TestCase):

    def test_parse_directory(self: "ParserTest"):
        parsed_args = parse_args(["test-directory"])

        self.assertEqual(parsed_args.directory, "test-directory")

    def test_parse_dispatch(self: "ParserTest"):
        self.assertTrue(parse_args(["test-directory", "-d"]).dispatch)
        self.assertTrue(parse_args(["test-directory", "--dispatch"]).dispatch)
        self.assertFalse(parse_args(["test-directory"]).dispatch)
