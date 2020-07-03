#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from derl.outputer import output


class OutputerTest(TestCase):

    def test_output_without_any_files(self: "OutputerTest"):
        with patch("sys.stdout", new=StringIO()) as fake_stdout:
            output([])
            self.assertTrue(fake_stdout.getvalue() == "")
