#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

from pathlib import Path
from unittest import TestCase

from derl.checker import _is_directory, is_text_file


class CheckerTest(TestCase):

    def test_is_directory(self: "CheckerTest"):
        self.assertTrue(_is_directory("tests/test-directory"))
        self.assertFalse(_is_directory("tests/not-existent-directory"))

    def test_is_text_file(self: "CheckerTest"):
        self.assertTrue(is_text_file(Path("tests/test-files/plain-text")))
        self.assertFalse(is_text_file(Path("tests/test-files/binary-data")))
