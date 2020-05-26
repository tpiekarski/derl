# -*- coding: utf-8 -*-

from derl.model.url import URL


class File:
    filename = None
    urls: None

    def __init__(self, filename):
        self.filename = filename
        self.urls = []

    def __str__(self):
        output_urls = ""

        for current_url in self.urls:
            output_urls += "\n - %s" % (current_url)

        return "{}:{}".format(self.filename, output_urls)

    def append(self, url, line_number):
        self.urls.append(URL(url, line_number))
