#!/usr/bin/env python

"""memcached.py.

Usage:
  memcached.py (--help)
  memcached.py (--version)
  memcached.py (-s | --server) MEMCACHEDSERVER (-c | --command) COMMAND (-k | --key) KEY
  memcached.py (-s | --server) MEMCACHEDSERVER (-c | --command) COMMAND (-k | --key) KEY (-v | --value) VALUE
  memcached.py (-s | --server) MEMCACHEDSERVER (-c | --command) COMMAND (-k | --key) KEY (-p | --port ) PORT
  memcached.py (-s | --server) MEMCACHEDSERVER (-c | --command) COMMAND (-k | --key) KEY (-v | --value) VALUE (-p | --port) PORT
  
Options:
  --help     Show this screen.
  --version     Show version.
  -s --server  Memcached server.
  -c --command  Memcached command.
  -k --key  key.
  -v --value  value.
  -p --port   Memcached port number.
"""

VERSION='0.1'

import sys

try:
  from docopt import docopt
except ImportError, e:
  print "Missing docopt module.  Install with: sudo pip install docopt"
  print "If you don't have pip, do this first: sudo easy_install pip"
  exit( 2 )

try:
  import memcache
except ImportError, e:
  print "Missing python-memcached module. Install with: sudo pip install python-memcached"
  print "If you don't have pip, do this first: sudo easy_install pip"
  exit( 2 )

def main( argv ):
  arguments = docopt(__doc__, version="memcached.py " + VERSION, options_first=False)
  print(arguments)

  port = '11211'

  if arguments['PORT'] is not None:
    port = arguments['PORT']

  print port

if __name__ == "__main__":
  main( sys.argv )

'''
import memcache
client = memcache.Client([('127.0.0.1', 11211)])
client.set("counter", "10")
client.incr("counter")
print "Counter was incremented on the server by 1, now it's %s" %
client.get("counter")
client.incr("counter", 9)
print "Counter was incremented on the server by 9, now it's %s" %
client.get("counter")
client.decr("counter")
print "Counter was decremented on the server by 1, now it's %s" %
client.get("counter")
'''