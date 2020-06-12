#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

class URL:
    url = None
    status_code = None
    line_number = None

    def __init__(self, url, line_number):
        self.url = url
        self.line_number = line_number

    def __str__(self):
        if self.status_code is None:
            format_string = "#{}: {}".format(self.line_number, self.url)
        else:
            format_string = "#{}: {}, {}".format(self.line_number, self.status_code, self.url)

        return format_string

    def __repr__(self):
        return self.__str__()
