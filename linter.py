#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Ivan Filenko
# Copyright (c) 2017 Ivan Filenko
#
# License: MIT
#

"""This module exports the Dockerfilelint plugin class."""

import json
from SublimeLinter.lint import Linter, util


class Dockerfilelint(Linter):
    """Provides an interface to dockerfilelint."""

    syntax = 'dockerfile'
    cmd = 'dockerfilelint --json'
    executable = 'dockerfilelint'
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 1.4.0'
    config_file = ('.dockerfilelintrc', '~')

    # The following regex parses text in format <file>:<line>:<error>:<message>\n
    #
    # Possible Bug & Deprecation marked as errors
    #
    # Optimization & Clarity marked as warnings

    regex = (
        r'^.+?:(?P<line>\d+):'
        r'(?:(?P<error>Possible Bug|Deprecation|)|(?P<warning>Optimization|Clarity|)):'
        r'(?P<message>.+)$\r?\n'
    )
    multiline = True
    error_stream = util.STREAM_STDOUT
    selectors = {}
    defaults = {}

    def run(self, cmd, code):
        output = super().run(self, cmd, code)
        return self.format(output)

    def format(self, output):
        """Formats json output to text <file>:<line>:<error>:<message>\n"""

        json = json.loads(output)
        filename = json['files'][0]['file']
        formatted_lines = []

        for issue in json['files'][0]['issues']:
            message = issue['description'].split('.')[0]
            formatted_lines.append(''.join([filename, ':', issue['line'], ':', issue['category'], ':', message, "\n"]))
        return ''.join(formatted_lines)

