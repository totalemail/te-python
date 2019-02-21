#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `te_python` CLI."""

import click
from click.testing import CliRunner

from te_python import cli


def test_te_python_cli():
    runner = CliRunner()
    result = runner.invoke(cli.main, ['--version'])
    assert result.exit_code == 0
    assert result.output == 'te_python version: 0.1.1\n'
