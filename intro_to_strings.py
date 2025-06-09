# intro_to_strings.py

# lower case with uderscores (snakes) between subsequent words
# snake_case
first_name = "Aidan"

#FirstName = "Aidan"
#firstName = "Aidan"
#first-Name = "Aidan"


last_name = 'Killeen'
last_name = 'O\'Sullivan'


# escape character \
message = "Press the \"red\" button"
print (message)
message = 'Press the "red" button'
print (message)
last_name = "O'Sullivan"

# \n - newline
# \t - tab
# \r - carriage return

file_name = "c:\\my documents\\personal\\file.txt"
print (file_name)


name = "Aidan"

print ("Welcome " + name)


count = 100

# use str to convert things to strings
print ("The count is " + str(count))

# f - strings

print (f"The count is { count }")

a = 10
b = 20

print (" " + str(a) + " + " + str(b) + " = " + str(a + b))

# more elegant using f strings:
print (f" { a } + { b } = { a+b }")


a = 22
b = 7

pi = a / b

print (f"{a} / {b} = {pi:0.5}")

s = "abcdef"
print (len(s))

print (s[0])

for letter in s:
    print (letter)


    























 























