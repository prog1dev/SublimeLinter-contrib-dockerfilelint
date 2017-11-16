SublimeLinter-contrib-dockerfilelint
=========================

This linter plugin for [SublimeLinter](http://sublimelinter.readthedocs.org) provides an interface to [dockerfilelint](https://www.npmjs.com/package/dockerfilelint). It will be used with files that have the “Dockerfile” syntax.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here](http://sublimelinter.readthedocs.org/en/latest/installation.html).

### Linter installation
Before installing this plugin, you must ensure that `dockerfilelint` is installed on your system. To install `dockerfilelint`, do the following:

1. Install [Node.js](http://nodejs.org) (and [npm](https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager) on Linux).

2. Install `dockerfilelint` by typing the following in a terminal:
  ```
    npm install -g dockerfilelint@">=1.4.0"
  ```

3. If you are using `nvm` and `zsh`, ensure that the line to load `nvm` is in `.zshenv` or `.zprofile` and not `.zshrc`.(reason: [here](http://www.sublimelinter.com/en/latest/installation.html) and [here](https://github.com/SublimeLinter/SublimeLinter3/issues/128))

**Note:** This plugin requires `dockerfilelint` 1.4.0 or later.

### Linter configuration
In order for `dockerfilelint` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through [“Validating your PATH”](http://www.sublimelinter.com/en/latest/troubleshooting.html#validating-your-path) in the documentation.

Once `dockerfilelint` is installed and configured, you can proceed to install the SublimeLinter-contrib-dockerfilelint plugin if it is not yet installed.

### Plugin installation
As for now this plugin is not officially approved by [SublimeLinter](https://github.com/SublimeLinter) members. So the only way to use this plugin is to install from source.

**For MacOS users:**

1. In you terminal run `cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/ && git clone git@github.com:prog1dev/SublimeLinter-contrib-dockerfilelint.git`
2. Restart your Sublime Text 3 editor
3. Enjoy!

## Settings
For general information on how SublimeLinter works with settings, please see [Settings](http://sublimelinter.readthedocs.org/en/latest/settings.html). For information on generic linter settings, please see [Linter Settings](http://sublimelinter.readthedocs.org/en/latest/linter_settings.html).

You can configure `dockerfilelint` options in the way you would from the command line, with `.dockerfilelintrc` file. For more information, see the [dockerfilelint configuring section](https://www.npmjs.com/package/dockerfilelint#configuring). The linter plugin does this by searching for a `.dockerfilelintrc` file itself, just as `dockerfilelint` does from the command line.

The path to the `.dockerfilelintrc` file is cached, meaning if you create a new `.dockerfilelintrc` that should have precedence over the previous one. You need to clear the cache for the linter to use the new `.dockerfilelintrc`. You can clear the cache by going to: Tools > SublimeLinter > Clear Caches.

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
2. Hack on a separate topic branch created from the latest `master`.
3. Commit and push the topic branch.
4. Make a pull request.
5. Be patient.  ;-)

Please note that modications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.

Thank you for helping out!
