# module_investigation.py


def greet (name):
    return f"Welcome {name}"


# code for testing the module
# only run if this module is the first module
# otherwise it is ignored
if __name__ == "__main__":
    for name in ["Alice", "Bob", "Carol", "Dan"]:
        print (greet (name))



