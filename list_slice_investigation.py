# list_slice_investigation.py


list = ["one", "two", "three", "four", "five", "six"]

print (list[0])

print (len(list))

print (list[1:4])
print (list[:3])
print (list[3:])

# negative index - work from the end
print (list[-1]) # last item in the list
print (list[-2:])

# step
print (list[2:5:2])
print (list[::2])
print ("-" * 25)
print (list)
print(list[::-1]) # reverse the string

# you can change the values in a list
list[0] = "CHANGED"

print(list)



