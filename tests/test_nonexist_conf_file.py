#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from te_python import utility


def test_te_python_initialization_with_nonexist_conf_file():
    with pytest.raises(FileNotFoundError):
        utility.headers, utility.base_api_url = utility.init('~/foo/nonexist')
