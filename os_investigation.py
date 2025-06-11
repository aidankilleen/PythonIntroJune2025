# os_investigation.py

import os

home_folder = os.getcwd()

print (home_folder)

os.chdir("testfolder")

with open("test.txt", "r") as f:

    lines = f.readlines()

    print (lines)

os.chdir(home_folder)

files = os.listdir()


for f in files:
    print (f"{f} is a { "folder" if os.path.isdir(f) else "file"}")

stats = os.stat("hello_world.py")
print (stats)

"""
print (files)
"""

# launch notepad with hello_world.py open for editing
os.system("notepad hello_world.py")






