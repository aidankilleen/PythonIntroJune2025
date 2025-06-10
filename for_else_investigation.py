# for_else_investigation.py

from random import randint

for i in range(10):
    r = randint(1, 10)
    if r == 3:
        continue # ends this iteration of the loop

    print (f"{i} - {r}")

    if r == 7:
        print ("finish the loop")
        break   # ends the loop immediately

else:
    # else gets triggered if the loop completes normally without encountering a break
    print ("Else block triggered")

print ("finished")

    

