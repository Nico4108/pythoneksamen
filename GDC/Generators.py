# A simple generator for Fibonacci Numbers
def fib(limit):
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1

    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        #return a, b
        a, b = b, a + b


    # Create a generator object


x = fib(10)

# Iterating over the generator object using next
print(x.__next__())  # In Python 3, __next__()
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())

'''print(x)
print(x)
print(x)
print(x)
print(x)
print(x)'''


# --------------------------------------------------------------------------------------------------------------------
# Iterating over the generator object using for
# in loop.
fi = fib(10000)
print("\nUsing for in loop")

listtt = []
for i in fi:
    print(i)
    if len(str(i)) < 4:
        listtt.append(i)
        #fi.throw(ValueError("Im tooooo hiiiiigh!!"))
        #fi.close()
print(listtt)


# --------------------------------------------------------------------------------------------------------------------
# Generator comprehension
fi = fib(10000)
comp_gen = (i for i in fi if len(str(i)) < 4)
print(list(comp_gen))

