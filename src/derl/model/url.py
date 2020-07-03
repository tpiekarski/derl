#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

_CONTEXT_OUTPUT_MAP = {0: "", 1: "  {}\n", 2: "  {}\n  {}\n", 3: "  {}\n  {}\n  {}\n"}


def _normalize_context(context: list) -> list:
    normalized_context = []

    for current_line in context:
        normalized_context.append(current_line.replace("\n", ""))

    return normalized_context


class URL:
    location = None
    status_code = None
    line_number = None
    context = []

    def __init__(self: "URL", location: str, line_number: int):
        self.location = location
        self.line_number = line_number

    def __str__(self: "URL") -> str:
        if self.status_code is None:
            output = "{}, {}".format(self.line_number, self.location)
        else:
            output = "{}, {}, {}".format(self.line_number, self.status_code, self.location)

        if self.is_context_present():
            output += "\n"
            output += _CONTEXT_OUTPUT_MAP.get(len(self.context)).format(*self.context)

        return output

    def __repr__(self: "URL") -> str:
        return self.__str__()

    def is_context_present(self: "URL") -> bool:
        return len(self.context) > 0

    def set_context(self: "URL", context: list):
        self.context = _normalize_context(context)
