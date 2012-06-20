#!/usr/bin/env python

import subprocess
import sys
import os

def up(dir_):
  match = True
  cwd = os.getcwd()

  # Start one level up from the current directory.
  head, tail = os.path.split(cwd)

  while 1:
    head, tail = os.path.split(head)
    if dir_ in tail:
      print os.path.join(head, tail)
      #os.chdir(os.path.join(head, tail))
      #print 'subprocess'
      #subprocess.Popen("cd " + os.path.join(head, tail), shell=True)
      #print os.getcwd()
      match = True
      break
    elif head == "/":
      match = False
      break

  if not match:
    sys.exit("No directory found")

if __name__ == "__main__":
  args = sys.argv[1:]

  if args:
    if args[0] in ["-h", "--help"]:
      print 
      print "$ pwd"
      print "/usr/local/adnxs/hbui/application/controllers"
      print "$ up adnxs"
      print "$ pwd"
      print "/usr/local/adnxs"
      print 
      print "---"
      print 
      print "$ pwd"
      print "/usr/local/adnxs/hbui/application/controllers"
      print "$ up loc"
      print "$ pwd"
      print "/usr/local"
      print 
      print "---"
      print 
      print "$ pwd"
      print "/usr/local/adnxs/hbui/application/controllers"
      print "$ up foo"
      print "No matching directories found"
      print "$ pwd"
      print "/usr/local/adnxs/hbui/application/controllers"
      print 
    else:
      up(args[0])
  else:
    sys.exit("You must specify a directory to go 'up' to.")
