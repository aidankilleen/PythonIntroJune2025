# tuple_investigation.py

# tuple is an immutable list - i.e. a list where you can't change the values


l = ["one", "two", "three", "four", "five", "six"]
t = ("one", "two", "three", "four", "five", "six")

print (l)
print (t)

print (t[0])
print (len(t))
print (t[0])

print (t[1:4])
print (t[:3])
print (t[3:])

print (t[-1])
print (t[-2:])

print (t[2:5:2])
print (t[::2])

print (t[::-1])

# you cannot change the values in a tuple
t[0] = "CHANGED"
print (t)








