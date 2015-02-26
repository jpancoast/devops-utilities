#!/usr/bin/env python

"""
Basic domain bruteforcer

Usage:
  naval_fate.py (--speed=<kn>) (--file=<file>)

Options:
  --speed=<kn>  Speed in knots.
  --file=<file>  File.
"""

VERSION = '0.1'

import sys

from docopt import docopt



if __name__ == "__main__":
  arguments = docopt(__doc__, version="test_non_positional.py " + VERSION, options_first=False)
#  arguments = docopt(__doc__, version='0.1a')
  print(arguments)