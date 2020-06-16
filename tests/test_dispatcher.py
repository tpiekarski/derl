#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

from unittest import TestCase

from derl.dispatcher import request
from derl.model.file import File


class DispatcherTest(TestCase):

    def test_request(self):
        test_file = File("test-file.txt")
        test_file.append("http://www.python.org/", 14)
        test_files = [test_file]

        files = request(test_files)

        self.assertEqual(files[0].urls[0].status_code, 200)

    def test_dispatcher_without_any_files(self):
        self.assertEqual(request([]), [])
