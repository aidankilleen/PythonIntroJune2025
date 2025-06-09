# dictionary_investigation.py

d = {
    "name": "Aidan",
    "title": "Python Trainer",
    "phone": "087 1231231"
}

print (d)

print (d["name"])
print (d["phone"])

dkeys = d.keys()

print (dkeys)

dvalues = d.values()

print (dvalues)
print ("-" * 25)
# iterate through the keys in a dictionary 
for item in d:
    print (f"{item}:{d[item]}")

print ("-" * 25)

# dictionaries are mutable
d["name"] = "AIDAN"

print (d)

# you can add new keys
d["address"] = "Cork"

print (d)








