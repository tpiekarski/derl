# -*- coding: utf-8 -*-

import requests


class URL:
    url = None
    status_code = None
    line_number = None

    def __init__(self, url, line_number):
        self.url = url
        self.line_number = line_number
        self.status_code = self.get_status_code(url)

    def get_status_code(self, url):
        # request = requests.get(url)
        # return request.status_code
        return 0
