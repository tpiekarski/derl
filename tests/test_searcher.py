# -*- coding: utf-8 -*-

from unittest import TestCase

from derl.searcher import search_urls


class SearcherTest(TestCase):

    def test_search_urls_without_any_files(self):
        self.assertEqual(search_urls([]), [])
