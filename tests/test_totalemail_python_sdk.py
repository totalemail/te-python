#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `te_python` module."""

import pytest

from te_python import te_python


@pytest.fixture
def response():
    return "foo bar"


def test_te_python_initialization():
    assert 1 == 1
