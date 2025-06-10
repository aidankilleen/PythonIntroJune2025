# command_line_investigation.py

import sys

# print (sys.argv)

if len(sys.argv) < 2:
    print ("Usage:")
    print ("Please supply a filename")
    exit()

with open(sys.argv[1], "r") as f:
    lines = f.readlines()
    print (f"Line count:{ len(lines)}")