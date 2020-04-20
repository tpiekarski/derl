# -*- coding: utf-8 -*-

import pytest
from derl.skeleton import sb

__author__ = "Thomas Piekarski"
__copyright__ = "Thomas Piekarski"
__license__ = "mit"


def test_sb():
    assert sb() == "Hello"
