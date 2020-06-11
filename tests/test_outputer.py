# -*- coding: utf-8 -*-

from unittest import TestCase
from unittest.mock import patch
from io import StringIO

from derl.outputer import output


class OutputerTest(TestCase):

    def test_output_without_any_files(self):
        with patch("sys.stdout", new=StringIO()) as fake_stdout:
            output([])
            self.assertTrue(fake_stdout.getvalue() == "")