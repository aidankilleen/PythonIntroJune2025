# inline_conditional_investigation.py

from random import randint

# inline conditional statements
r = randint(1, 100)

if r < 50:
    print (f"{r} is small")
else:
    print (f"{r} is large")

print ("small" if r < 50 else "large") # equivalent to ternary operation in other languages?:
print (f"{r} is {"small" if r < 50 else "large"}")


if r < 30:
    print (f"{r} is small")
elif r < 60:
    print (f"{r} is medium")
else:
    print (f"{r} is large")

print (f"{r} is {"small" if r < 30 else "medium" if r < 60 else "large"}")

