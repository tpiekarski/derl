# -*- coding: utf-8 -*-

from derl.model.url import URL


class File:
    filename = None
    path = None
    urls: None

    def __init__(self, filename, path):
        self.filename = filename
        self.path = path
        self.urls = []

    def append(self, url, line_number):
        self.urls.append(URL(url, line_number))
