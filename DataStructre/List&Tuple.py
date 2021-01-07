# Tuple
tup_num = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

# List
list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print('a =', tup_num.__sizeof__())
print('b =', list_num.__sizeof__())

list_num[2] = 5
print(list_num)

# Kan ikke da Tuple ikke er mutible
#tup_num[2] = 5
#print(tup_num)


# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
def front_x(words):
    x = []
    y = []
    for w in words:
        if w[0] == 'x':
            x.append(w)
        else:
            y.append(w)

    print(sorted(x) + sorted(y))


front_x(['xix', 'xyz', 'apple', 'hanadu', 'aardvark', 'xxaaa', 'Claus'])


# return a list sorted in increasing
# order by the last element in each tuple.
def sort_last(tuples):
    def last_element(t):
        return t[-1]

    print(sorted(tuples, key=last_element))


sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2), (10, 2), (20, 50)])


# List Comprehension

# List of capital letters in the english alphabet
print([chr(i) for i in range(65, 91)])


def without_comprehensions():

    # Constructing output list WITHOUT using List comprehensions
    input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

    output_list = []

    # Using loop for constructing output list
    for var in input_list:
        if var % 2 == 0:
            output_list.append(var)

    print("Output List using for loop:", output_list)


def with_comprehensions():

    # Using List comprehensions for constructing output list
    input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

    # Dette er en list comprehension, en one-liner
    list_using_comp = [var for var in input_list if var % 2 == 0]

    print("Output List using list comprehensions:",
          list_using_comp)


without_comprehensions()
with_comprehensions()
