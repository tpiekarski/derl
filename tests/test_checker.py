# -*- coding: utf-8 -*-

from unittest import TestCase

from derl.checker import *


class CheckerTest(TestCase):

    def test_is_text_file(self):
        self.assertTrue(is_text_file("tests/test-files/plain-text"))
        self.assertFalse(is_text_file("tests/test-files/binary-data"))

    def test_is_directory(self):
        self.assertTrue(is_directory("tests/test-directory"))
        self.assertFalse(is_directory("tests/not-existent-directory"))
