# The way to do dictionary comprehension in Python is to be able to
# access the key objects and the value objects of a dictionary.
# You can simply use the built-in methods for the same:

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Put all keys of `dict1` in a list and returns the list
print(dict1.keys())
# Put all values saved in `dict1` in a list and returns the list
print(dict1.values())
# Access each key-value pair
print(dict1.items())

# Double each value in the dictionary
# Dette er en dictionary comprehension, en one-liner
double_dict1 = {k: v*2 for (k, v) in dict1.items()}
print(double_dict1)

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
for key in list(Dict.keys()):
    if key in list(Boys.keys()):
        print(True)
    else:
        print(False)

# Den er der næsten.
# a = {key for key in list(Dict.keys()) if key in list(Boys.keys())}
# b = {key if key in list(Boys.keys()) else False for key in list(Dict.keys())}
# c = {key in list(Boys.keys()) if key else False for key in list(Dict.keys())}
# print(c)

