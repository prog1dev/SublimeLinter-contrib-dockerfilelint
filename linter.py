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

    cmd = 'dockerfilelint --json'
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
    defaults = {
        'selector': 'source.dockerfile'
    }

    def run(self, cmd, code):
        output = super().run(cmd, code)
        return self.format(output)

    def format(self, output):
        """Formats json output to text <file>:<line>:<error>:<message>\n"""

        json_output = json.loads(output)
        formatted_lines = []

        for issue in json_output['files'][0]['issues']:
            file = json_output['files'][0]['file']
            line = issue['line']
            error = issue['category']
            message = issue['description']

            formatted_lines.append(''.join([file, ':', line, ':', error, ':', message, "\n"]))

        return ''.join(formatted_lines)
