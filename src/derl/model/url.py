# -*- coding: utf-8 -*-

import requests

_DEFAULT_TIMEOUT = 1


class URL:
    url = None
    status_code = None
    line_number = None

    def __init__(self, url, line_number):
        self.url = url
        self.line_number = line_number
        self.status_code = self.get_status_code(url)

    def __str__(self):
        return "{}, {}".format(self.url, self.status_code)

    def get_status_code(self, url):
        request = requests.get(url, timeout=_DEFAULT_TIMEOUT)

        return request.status_code
