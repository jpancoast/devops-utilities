#!/usr/bin/env python

"""
Basic domain bruteforcer

Usage:
  naval_fate.py (--speed=<kn>) (--file=<file>)

Options:
  -s, --speed=<kn>  Speed in knots.
  -f, --file=<file>  File.
"""

VERSION = '0.1'

import sys

from docopt import docopt



if __name__ == "__main__":
  arguments = docopt(__doc__, version="test_non_positional.py " + VERSION, options_first=False)
  print(arguments)