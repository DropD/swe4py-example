# SPDX-FileCopyrightText: 2025-present DropD <rico.haeuselmann@gmail.com>
#
# SPDX-License-Identifier: MIT
import click

from swe4py_example.__about__ import __version__


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name="swe4py-example")
def swe4py_example():
    click.echo("Hello world!")
