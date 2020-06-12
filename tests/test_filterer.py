# -*- coding: utf-8 -*-

from unittest import TestCase

from derl.filterer import filter_not_matching
from derl.model.file import File


class FiltererTest(TestCase):

    def test_filter_not_matching(self):
        file_with_url = File("a.txt")
        file_with_url.append("http://www.somewhere.com/", 0)
        file_without_url = File("b.txt")

        files = [file_with_url, file_without_url]
        filtered_files = filter_not_matching(files)

        self.assertEqual(len(files), 2)
        self.assertEqual(len(filtered_files), 1)
