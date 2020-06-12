#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

from derl.model.url import URL


class File:
    filename = None
    urls: []

    def __init__(self, filename):
        self.filename = filename
        self.urls = []

    def __str__(self):
        output_urls = ""

        for current_url in self.urls:
            output_urls += "\n - %s" % (current_url)

        return "{}:{}".format(self.filename, output_urls)

    def __repr__(self):
        return self.__str__()

    def append(self, url, line_number):
        self.urls.append(URL(url, line_number))

    def contains_urls(self):
        return len(self.urls) > 0
