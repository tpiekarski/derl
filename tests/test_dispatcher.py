#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

from unittest import TestCase

from unittest.mock import patch
from requests.exceptions import ConnectionError as RequestConnectionError, Timeout, TooManyRedirects

from derl.dispatcher import request
from derl.model.file import File


def _build_test_files():
    test_file = File("test-file.txt")
    test_file.append("http://www.python.org/", 14)

    return [test_file]


class DispatcherTest(TestCase):

    def test_request(self):
        files = request(_build_test_files())

        self.assertEqual(files[0].urls[0].status_code, 200)

    def test_dispatcher_without_any_files(self):
        self.assertEqual(request([]), [])

    @patch("requests.get")
    def test_timeout(self, mocked_get):
        mocked_get.side_effect = Timeout

        files = request(_build_test_files())
        self.assertEqual(files[0].urls[0].status_code, 0)

    @patch("requests.get")
    def test_too_many_redirects(self, mocked_get):
        mocked_get.side_effect = TooManyRedirects

        files = request(_build_test_files())
        self.assertEqual(files[0].urls[0].status_code, 0)

    @patch("requests.get")
    def test_connection_error(self, mocked_get):
        mocked_get.side_effect = RequestConnectionError

        files = request(_build_test_files())
        self.assertEqual(files[0].urls[0].status_code, 0)
