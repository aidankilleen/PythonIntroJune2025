# stdin_input_investigation.py

import sys

f = sys.stdin

count = 0

for line in f:
    count = count + 1
    print (f"- {line}", end="")

print (f"Line count:{count}")

