# lc.py
# line counter utiltity

import sys

f = sys.stdin
if len(sys.argv) == 2:
    f = open(sys.argv[1], "r")

count = 0
for line in f:
    count = count + 1
 
print (count)

