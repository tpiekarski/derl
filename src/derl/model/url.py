#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

_CONTEXT_OUTPUT_MAP = {0: "", 1: "  {}\n", 2: "  {}\n  {}\n", 3: "  {}\n  {}\n  {}\n"}


class URL:
    url = None
    status_code = None
    line_number = None
    context = []

    def __init__(self, url, line_number):
        self.url = url
        self.line_number = line_number

    def __str__(self):
        if self.status_code is None:
            output = "{}, {}".format(self.line_number, self.url)
        else:
            output = "{}, {}, {}".format(self.line_number, self.status_code, self.url)

        if self.is_context_present():
            output += "\n"
            output += _CONTEXT_OUTPUT_MAP.get(len(self.context)).format(*self.context)

        return output

    def __repr__(self):
        return self.__str__()

    def is_context_present(self):
        return len(self.context)

    def normalize_context(self, context):
        normalized_context = []

        for current_line in context:
            normalized_context.append(current_line.replace("\n", ""))

        return normalized_context

    def set_context(self, context):
        self.context = self.normalize_context(context)
