# -*- coding: utf-8 -*-

import pytest
from derl.skeleton import check_directory, process_directory, parse_args

__author__ = "Thomas Piekarski"
__copyright__ = "Thomas Piekarski"
__license__ = "mit"


def test_parse_directory():
    raw_args = ["/test"]
    parsed_args = parse_args(raw_args)

    assert parsed_args.directory == "/test"


def test_check_directory():
    assert check_directory("/test") == True


def test_process_directory():
    assert process_directory("/test") == []
