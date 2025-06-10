# lc.py
# line counter utiltity

import sys

f = sys.stdin
if len(sys.argv) == 2:

    if sys.argv[1] == "-h":
        print (
"""
lc.py
Usage:
lc.py [OPTION] [FILE]
count the lines in FILE or STDIN if FILE omitted
Options:
-h - show this help message
""")
        exit()

    else:
        try:
            f = open(sys.argv[1], "r")
        except:
            print (f"file not found {sys.argv[1]}")
            exit()

count = 0
for line in f:
    count = count + 1
 
print (count)

