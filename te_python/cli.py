#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""TotalEmail Python SDK"""

import click

from .__init__ import __version__ as VERSION


@click.command()
@click.option('--version', is_flag=True, help='Print the version of the package')
def main(version):
    """CLI interface for te_python"""
    if version:
        print("te_python version: {}".format(VERSION))


if __name__ == "__main__":
    main()
