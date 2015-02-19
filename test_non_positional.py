#!/usr/bin/env python

"""test_non_positional.py.

Usage:
  test_non_positional.py (--help)
  test_non_positional.py (--version)
  test_non_positional.py (-s | --server) MEMCACHEDSERVER (-c | --command) COMMAND 
  test_non_positional.py (-c | --command) COMMAND (-s | --server) MEMCACHEDSERVER
  
Options:
  --help     Show this screen.
  --version     Show version.
  -s --server  Memcached server.
  -c --command  Memcached command.
"""

VERSION='0.1'

import sys

try:
  from docopt import docopt
except ImportError, e:
  print "Missing docopt module.  Install with: sudo pip install docopt"
  print "If you don't have pip, do this first: sudo easy_install pip"
  exit( 2 )



def main( argv ):
  arguments = docopt(__doc__, version="test_non_positional.py " + VERSION, options_first=False)
  print(arguments)

if __name__ == "__main__":
  main( sys.argv )
