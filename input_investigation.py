# input_investigation.py

name = input("What is your name?")

print(f"Welcome {name}")

# nb - input always returns a string
a = input("Enter a number:")

print (a * 10)

# if you need a number you need to convert from a string

a = int(input("Enter a number:"))

print (a * 10)


num = input("Enter a number:")

if num.isnumeric():
    print (int(num) * 10)
else:
    print ("That's not a number")





