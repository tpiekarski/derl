#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from pytest import raises

from conftest import _TEST_DIRECTORY
from derl.main import main


class MainTest(TestCase):

    def _reference_testing(self, arguments, reference):
        with patch("sys.stdout", new=StringIO()) as fake_stdout:
            with open(reference, "r") as opened_reference:
                with raises(SystemExit) as wrapped_exit:
                    main(arguments)

                    self.assertEqual(wrapped_exit.type, SystemExit)
                    self.assertEqual(wrapped_exit.value.code, 0)

                self.assertEqual(fake_stdout.getvalue(), opened_reference.read())

    def test_main_without_dispatch(self):
        self._reference_testing([_TEST_DIRECTORY], "tests/references/output-without-dispatch.out")

    def test_main_with_dispatch(self):
        self._reference_testing(["--dispatch", _TEST_DIRECTORY], "tests/references/output-with-dispatch.out")

    def test_main_with_not_existing_directory(self):
        with raises(SystemExit) as wrapped_exit:
            main(["tests/not-existing"])

        self.assertEqual(wrapped_exit.type, SystemExit)
        self.assertEqual(wrapped_exit.value.code, -1)
