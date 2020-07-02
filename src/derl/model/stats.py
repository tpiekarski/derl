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
        output = ""

        output += "---\n"
        output += "Directories:\t{0}\n".format(self.directories)
        output += "Files:\t\t{0}\n".format(self.files)
        output += "Lines:\t\t{0}\n".format(self.lines)
        output += "Tokens:\t\t{0}\n".format(self.tokens)
        output += "URLs:\t\t{0}\n".format(self.urls)
        output += "Requests:\t{0}\n".format(self.requests)

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
