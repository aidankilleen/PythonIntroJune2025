# building_blocks.py
# By: Aidan
# Date: 9/6/2025

# building block #1 - Comment


# building block #2 - variables
# no need to declare variables

name = "Aidan"
i = 10
f = 10.123456

print ("hello", name) 

n = 123438752845623984752873452789345662379845689273658237734

n = 99
print (n)
n = "ninety nine"

print(n)

# building block #3 - expressions

a = 100
b = 200

# PEMDAS - parenthesis, exponentes, Multiplication, Division, Addition, Subtraction
answer = a + ((b * 100) / (23 * 37))

# you can multiply a string
print ("*" * 25)

# building block #4 - array / list
list = [2, 3, 5, 1, 6, 2]

print(list[1]) # item with index 0 is the first item

print (len(list))

#print (list[99]) # can't access item 99 in a list with 6 items
#asdasdf()

# NB:python is case-sensitive
print("hello")

# items in a list don't have to be the same
mixed_list = [1, 1.1, "one", [1, 1, 1]]
  

# building block #5 - loop

# doing things repetively

list = [3, 4, 2, 6, 1, 7, 6, 10]

for number in list:
    print (number)
    print ("-----")
# nb - in python the indentation is part of the syntax

# while loop
i = 0
while i < len(list):
    print (list[i])
    i = i + 1


print ("starting")
i = 0
answer = 0
while i < 1000000:
    answer = answer + i
    i = i + 1

print (answer)


# building block # 6 - conditions

# n=2 is an assignment 
# n==2 is a comparision
for number in list:

    if number % 2 == 0:
        print (number, "is even")
    else:
        print (number, "is odd")

for number in list:
    if number < 4:
        print (number, "is small")
    elif number < 7:
        print (number, "is medium")
    else:
        print (number, "is large")


# building #7 - functions
print("print is a function that prints things out")

len("is a function that counts how many things are in a list / length of a string")

# built-in functions
# standard library functions - installed by default
# 3rd party library functions - need an separate install
# user-defined functions

def greet(name):
    print ("Hello " + name)


greet("Aidan")

names = ["Alice", "Bob", "Carol", "Dan"]

for name in names:
    greet(name)


# building block #8 - Objects
# string is an object
# an object has value(s) / properties / member variables
# an object has functions / methods
message = "this is a string"

print (message)

print (message.upper())





































































