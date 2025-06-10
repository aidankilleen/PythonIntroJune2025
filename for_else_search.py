# for_else_search.py

names = ["Alice", "Bob", "Davidx", "Carol", "Dan"]

for name in names:

    if name == "David":
        print ("Found David")
        break

else:
    print ("David not found")

# redo this using while

i = 0

while i < len(names):
    if names[i] == "David":
        print ("Found David")
        break
    i += 1
else:
    print ("David not found")




