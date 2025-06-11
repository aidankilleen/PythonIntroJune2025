# recursion_investigation.py
# a function that calls itself
import time

def countdown (n):

    if n <= 0:
        print ("Blastoff")

    else:
        print (n)
        time.sleep(1)
        countdown(n-1)

countdown(5)





#def some_function():
#    if somecondition :
#        some_function() # infinite loop
#    else:
#        finished


