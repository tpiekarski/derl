# -*- coding: utf-8 -*-

import pytest
from derl.skeleton import check_directory, process_directory, parse_args

__author__ = "Thomas Piekarski"
__copyright__ = "Thomas Piekarski"
__license__ = "mit"

_TEST_DIRECTORY = "tests/test-directory"


def test_parse_directory():
    raw_args = [_TEST_DIRECTORY]
    parsed_args = parse_args(raw_args)

    assert parsed_args.directory == _TEST_DIRECTORY


def test_check_directory():
    assert check_directory(_TEST_DIRECTORY) == True
    assert check_directory("non-existend-directory") == False


def test_process_directory():
    assert process_directory(_TEST_DIRECTORY) == []
