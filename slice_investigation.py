# slice_investigation.py


message = "this is a message!"


print (f"Length:{len(message)}")

print(message[0])

print(message[5:7])
print(message[10:17])

# you can leave out either number
# assumes 0 if you leave out first number
print (message[:7])
#assumes end if you leave out the second number
print (message[7:])


# you can use negative index
# -1 is the last character
print (message[-1])
print (message[-10:])


message = "abcdefghijklmnop"
print (message[2:10:2])
print (message[2:10:3])

message = "01234567890"

print (message[2:8:2])

print (message[::2])

# "pythonic" way of reversing a string
print (message[::-1])


number = "1234"

print (number.isnumeric())

print (number.isnumeric)

number = "abcdefghik"
if number.isnumeric:
    print ("number is numeric")





