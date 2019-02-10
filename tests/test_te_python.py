#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `te_python` module."""

from te_python import te_python


def test_te_python_initialization():
    response = te_python.email_get_details('a53b7747d6bd3f59076d63469d92924e00f407ff472e5a539936453185ecca6c')
    assert isinstance(response, dict)
