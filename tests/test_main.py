#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from pytest import raises

from derl.checker import _INVALID_DIRECTORY, _INVALID_RETRY, _INVALID_TIMEOUT
from derl.main import main, run
from derl.tracker import get_tracker
from conftest import _TEST_DIRECTORY, _TEST_REQUEST_RETRIES, _TEST_REQUESTS_TIMEOUT

_tracker = get_tracker()

_TEST_ARGUMENTS = [
    "--retry", str(_TEST_REQUEST_RETRIES),
    "--timeout", str(_TEST_REQUESTS_TIMEOUT)
]


class MainTest(TestCase):

    maxDiff = None

    def _reference_testing(self, arguments, reference):
        with patch("sys.stdout", new=StringIO()) as fake_stdout:
            with open(reference, "r") as opened_reference:
                with raises(SystemExit) as wrapped_exit:
                    main(_TEST_ARGUMENTS + arguments)

                self.assertEqual(wrapped_exit.type, SystemExit)
                self.assertEqual(wrapped_exit.value.code, 0)
                self.assertEqual(fake_stdout.getvalue(), opened_reference.read())

    def test_main_without_context_without_dispatch(self):
        self._reference_testing([_TEST_DIRECTORY], "tests/references/output-without-context-without-dispatch.out")

    def test_main_with_context_without_dispatch(self):
        self._reference_testing([_TEST_DIRECTORY, "--context"],
                                "tests/references/output-with-context-without-dispatch.out")

    def test_main_without_context_with_dispatch(self):
        self._reference_testing([_TEST_DIRECTORY, "--dispatch"],
                                "tests/references/output-without-context-with-dispatch.out")

    def test_main_with_context_with_dispatch(self):
        self._reference_testing([_TEST_DIRECTORY, "--context", "--dispatch"],
                                "tests/references/output-with-context-with-dispatch.out")

    def test_main_with_stats_without_dispatch(self):
        _tracker.set_test()
        _tracker.reset()

        self._reference_testing([_TEST_DIRECTORY, "--stats"],
                                "tests/references/output-with-stats-without-dispatch.out")

    def test_main_with_stats_with_dispatch(self):
        _tracker.set_test()
        _tracker.reset()

        self._reference_testing([_TEST_DIRECTORY, "--stats", "--dispatch"],
                                "tests/references/output-with-stats-with-dispatch.out")

    def test_main_with_not_existing_directory(self):
        with raises(SystemExit) as wrapped_exit:
            main(["tests/not-existing"])

        self.assertEqual(wrapped_exit.type, SystemExit)
        self.assertEqual(wrapped_exit.value.code, _INVALID_DIRECTORY)

    def test_main_with_invalid_timeout(self):
        with raises(SystemExit) as wrapped_exit:
            main(["--dispatch", "--timeout", "-5", _TEST_DIRECTORY])

        self.assertEqual(wrapped_exit.type, SystemExit)
        self.assertEqual(wrapped_exit.value.code, _INVALID_TIMEOUT)

    def test_main_with_invalid_retry(self):
        with raises(SystemExit) as wrapped_exit:
            main(["--dispatch", "--retry", "1000", _TEST_DIRECTORY])

        self.assertEqual(wrapped_exit.type, SystemExit)
        self.assertEqual(wrapped_exit.value.code, _INVALID_RETRY)

    def test_run(self):
        with patch("sys.stdout", new=StringIO()) as fake_stdout:
            with raises(SystemExit) as wrapped_exit:
                run()

            self.assertEqual(wrapped_exit.type, SystemExit)
            self.assertEqual(wrapped_exit.value.code, 2)
            self.assertEqual(fake_stdout.getvalue(), "")
