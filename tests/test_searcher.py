#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

from unittest import TestCase

from derl.searcher import search_urls


class SearcherTest(TestCase):

    def test_search_urls_without_any_files(self):
        self.assertEqual(search_urls([]), [])
