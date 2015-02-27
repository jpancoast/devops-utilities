#!/usr/bin/env python

"""
Insert or check for value in memcached cluster.

Usage:
    memcached.py [(--server=<server>) (--command=<command>) (--port=<port>) (--value=<value>)] (--key=<key>)

Options:
    --help  Show this screen
    --version   Show version
    -s, --server=<server>  Memcached server [default: localhost]
    -c, --command=<command>  Memcached command [default: get]
    -k, --key=<key>  Key.
    -v, --value=<value>  Value.
    -p, --port=<port>  Memcached server port [default: 11211].

"""

"""
Author: James Pancoast
Email: jpancoast@gmail.com 
twitter.com/jpancoast

Yeah, I know all this can be done by just telnetting to the memcached port and issuing commands, but I needed to have a reason to figure out docopt
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




class testclass():
  def __init__(self,arguments):
    (command, port, server, key, value) = self.parse_arguments(arguments)
    
    self.command = command
    self.key = key
    self.value = value

    self.memcacheclient = memcache.Client([(server, port)])

  def get_command(self):
    return self.command

  def parse_arguments(self,arguments):
    command = arguments['--command']
    key = arguments['--key']
    port = int(arguments['--port'])
    server = arguments['--server']
    value = arguments['--value']

    valid_commands = ['get', 'set', 'incr', 'decr', 'all']

    if command not in valid_commands:
      print "invalid command: " + command
      print "Command must be one of the following: " + str(valid_commands)
      exit(0)

    return ( command, port, server, key, value)

  def get(self):
    print "get"

  def set(self):
    print "set"

  def incr(self):
    print "incr"

  def decr(self):
    print "decr"

  def all(self):
    print "all"



def main( argv ):
  arguments = docopt(__doc__, version="memcached.py " + VERSION, options_first=False)

  testinstance = testclass(arguments)
  command = testinstance.get_command()

  try:
    func = getattr(testinstance,command)
  except AttributeError:
    print "Missing function " + command
  else:
    result = func()


def get():
  print "get"



if __name__ == "__main__":
  main( sys.argv )

'''
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