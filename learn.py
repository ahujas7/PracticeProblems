# Docstrings/Documentation Strings

def square(n):
    """Function which squares the input"""
    return n ** 2

print(square.__doc__)
# Function which squares the input

# Mutable, ordered, Slicing/indexing allowed
my_list = [1, 2, 1, 3, 9, 5]

# Immutable, Slicing/indexing allowed
my_string = 'Hello'

# Immutable, ordered, Slicing/indexing allowed
my_tuple = (1, 2, 2, 4, 5)

# Mutable, unordered, unique elements, no slicing/indexing allowed
my_set = {3, 2, 3, 4, 6}

# Mutable, unordered, unique keys
my_dict = {'a': 20, 'b': 1, 'c': 12}


