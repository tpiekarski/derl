#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#


class Stats():
    directories_processed = 0
    files_processed = 0
    lines_processed = 0
    requests_sent = 0
    tokens_processed = 0
    urls_processed = 0

    def __str__(self):
        output = ""

        output += "---\n"
        output += "Directories:\t{0}\n".format(self.directories_processed)
        output += "Files:\t\t{0}\n".format(self.files_processed)
        output += "Lines:\t\t{0}\n".format(self.lines_processed)
        output += "Tokens:\t\t{0}\n".format(self.tokens_processed)
        output += "URLs:\t\t{0}\n".format(self.urls_processed)
        output += "Requests:\t{0}\n".format(self.requests_sent)

        return output

    def __repr__(self):
        return self.__str__()

    def inc_directories(self):
        self.directories_processed += 1

    def inc_files(self):
        self.files_processed += 1

    def inc_lines(self):
        self.lines_processed += 1

    def inc_tokens(self):
        self.tokens_processed += 1

    def inc_urls(self):
        self.urls_processed += 1

    def inc_requests(self):
        self.requests_sent += 1
