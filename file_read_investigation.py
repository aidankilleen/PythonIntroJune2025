# file_read_investigation.py


# we will open our files using "with"
with open("test.txt", "r") as f:
    lines = f.readlines()

    print (lines)

# note no need for f.close()  



# traditional approach
f = open("test.txt", "r")
lines = f.readlines()
print (lines)
f.close()

