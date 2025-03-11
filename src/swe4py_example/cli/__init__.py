# SPDX-FileCopyrightText: 2025-present DropD <rico.haeuselmann@gmail.com>
#
# SPDX-License-Identifier: MIT
import click

from swe4py_example.__about__ import __version__


@click.command
@click.version_option(version=__version__, prog_name="swe4py-example")
def swe4py_example():
    click.echo("Hello world!")
