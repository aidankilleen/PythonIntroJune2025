# error_investigation.py
from random import randint
print ("starting...")
a = 10
b = 0
numbers = [1, 3, 5, 2, 4, 6]
number = "ninety nine"
answer = 0
r = randint(1, 5)

try:
    if r == 1:
        answer = int(number)
    elif r == 2:
        answer = numbers[6]
    elif r == 3:
        answer = a / b
    else:
        answer = 42 # no error
except ValueError:
    print (f"Can't convert {number}")
    answer = 99
except ZeroDivisionError:
    print ("You can't divide by zero")
    answer = 1
except Exception as ex:
    print ("something went wrong")
    print (ex)
finally:
    #this is code that gets executed in all cases - exception or not
    print (f"The answer is {answer}")
    
print ("finished")







# c -style of error handling using return codes
# glass is half empty style of programming
# if a > 0 and b >= 0:

#     r = DoSomething(a, b)

#     if r == -1:
#         print ("network error")
#     elif r == -2:
#         print ("user error")
#     elif r == -3:
#         print ("input error")
#     elif r == -4:
#         print ("file error")
#     else:
#         print ("all ok")

# r = DoSomethingElse()
# if r == -1:
#     print ("network error")
# elif r == -2:
#     print ("user error")
# elif r == -3:
#     print ("input error")
# elif r == -4:
#     print ("file error")
# else:
#     print ("all ok")


# Use Exceptions
# glass is half full 
# try:
#     doSomething()
#     doSomethingElse()

# except FileExistsError:
#     # handle the errors here
#     print ("file error")
# except MemoryError:
#     print ("memory error")
# except IndexError:
#     print ("index error")
# except:
#     print ("some other error")














