# file_write_investigation.py


# w will create the file if it doesn't exist
# it will overwrite the existing file if it does

# file mode "a" will append to an existing file
with open("names.txt", "w") as f:

    for name in ["Alice", "Bob", "Carol", "Dan"]:
        f.write(f"{name}\n")
