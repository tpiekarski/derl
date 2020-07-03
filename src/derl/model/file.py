#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

from derl.model.url import URL


class File:
    filename = None
    urls: []

    def __init__(self: "File", filename: str):
        self.filename = filename
        self.urls = []

    def __str__(self: "File") -> str:
        output = ""

        for current_url in self.urls:
            output += "{}:{}\n".format(self.filename, current_url)

        return output

    def __repr__(self: "File") -> str:
        return self.__str__()

    def append(self: "File", url: str, line_number: int):
        self.urls.append(URL(url, line_number))

    def contains_urls(self: "File") -> bool:
        return len(self.urls) > 0
