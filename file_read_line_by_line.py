# file_read_line_by_line.py

with open("names.txt", "r") as f:

    line = f.readline() # read the first line

    while line:

        print (line, end="")
        line = f.readline() # read the next line

print ("finished")

