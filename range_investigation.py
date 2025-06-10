# range_investigation.py

# start (inclusive), stop(exclusive), step
numbers = range(2, 10, 2)

for n in numbers:
    print (n)

print ("*" * 25)
for i in range(1, 11):
    print (i)

colours = ["red", "green", "blue", "orange"]

# we don't normally get an index
for i in range(len(colours)):
    print (colours[i])

# we normally do for <item> in <list>
for colour in colours:
    print (colour)


