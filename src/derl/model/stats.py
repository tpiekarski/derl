#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#


class Stats():
    directories = 0
    files = 0
    lines = 0
    requests = 0
    tokens = 0
    urls = 0

    def __str__(self):
        output = "Processed Directories/Files/Lines/Tokens/URLs: {0:d}/{1:d}/{2:d}/{3:d}/{4:d}".format(
            self.directories, self.files, self.lines, self.tokens, self.urls
        )

        if self.requests > 0:
            output += "\nSent HTTP GET Requests: {0:d}".format(self.urls)

        return output

    def __repr__(self):
        return self.__str__()

    def inc_directories(self):
        self.directories += 1

    def inc_files(self):
        self.files += 1

    def inc_lines(self):
        self.lines += 1

    def inc_tokens(self):
        self.tokens += 1

    def inc_urls(self):
        self.urls += 1

    def inc_requests(self):
        self.requests += 1
