# buggy_code.py

def divide(a, b):
    """Divides two numbers, but might have issues."""
    try:
        result = a / b
        return result
    except: # Catching all exceptions is bad practice
        return None

def process_list(my_list):
    """Processes a list, but might cause index errors."""
    for i in range(len(my_list) + 1): # Potential index out of range
        print(my_list[i])

def leaky_resource():
    """Opens a file but doesn't close it properly."""
    f = open("temp.txt", "w") # File not closed.
    f.write("Some data")

def unused_variable():
    """Defines a variable that is never used."""
    x = 10
    y = 20 # y is never used

def string_concat(a, b):
    """String concat using + in a loop"""
    result = ""
    for i in range(10):
        result = result + str(a) + str(b) # Inefficient string concat
    return result

def hardcoded_password():
    """Contains a hardcoded password."""
    password = "MySecretPassword" # Hardcoded password
    return password

def compare_floats(a, b):
    """Compares floats using ==."""
    if a == b: # Direct float comparison is unreliable
        return True
    else:
        return False

def empty_except():
    try:
        x = 1/0
    except Exception: # Empty except block
        pass

def redundant_if(a):
    if a == True:
        return True
    else:
        return False

def missing_docstring(a,b):
    return a + b
