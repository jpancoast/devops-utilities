#!/usr/bin/env python

"""test_non_positional.py.

Usage:
  test_non_positional.py [-s] MEMCACHEDSERVER [-c] COMMAND
  
Options:
  -s  Memcached server.
  -c  Memcached command.
"""

VERSION = '0.1'

import sys

try:
    from docopt import docopt
except ImportError, e:
    print "Missing docopt module.  Install with: sudo pip install docopt"
    print "If you don't have pip, do this first: sudo easy_install pip"
    exit(2)


def main(argv):
    arguments = docopt(
        __doc__, version="test_non_positional.py " + VERSION, options_first=False)
    print(arguments)

if __name__ == "__main__":
    main(sys.argv)
