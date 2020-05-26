# -*- coding: utf-8 -*-

class URL:
    url = None
    status_code = None
    line_number = None

    def __init__(self, url, line_number):
        self.url = url
        self.line_number = line_number

    def __str__(self):
        return "{}, {}".format(self.url, self.status_code)
