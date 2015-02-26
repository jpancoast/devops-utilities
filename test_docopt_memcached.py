#!/usr/bin/env python

"""
Insert or check for value in memcached cluster.

Usage:
    memcached.py (--server=<server>) (--command=<command>) (--key=<key>)
    memcached.py (--server=<server>) (--command=<command>) (--key=<key>) (--value=<value>)
    memcached.py (--server=<server>) (--command=<command>) (--key=<key>) (--port=<port>) 
    memcached.py (--server=<server>) (--command=<command>) (--key=<key>) (--port=<port>) (--value=<value>)

Options:
    --help  Show this screen
    --version   Show version
    -s, --server=<server>  Memcached server
    -c, --command=<command>  Memcached command
    -k, --key=<key>  Key.
    -v, --value=<value>  Value.
    -p, --port=<port>  Memcached server port.

"""

VERSION = '0.1'

import sys

from docopt import docopt



if __name__ == "__main__":
  arguments = docopt(__doc__, version="test_non_positional.py " + VERSION, options_first=False)
  print(arguments)