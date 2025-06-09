# function_profile.py

from time import time # #include in c equivalent

t_start = time()

print ("starting")
i = 0
answer = 0
while i < 10000000:
    answer = answer + i
    i = i + 1
print (answer)

t_end = time()

print (f"Time taken: {t_end - t_start} seconds")
