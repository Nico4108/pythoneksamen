import time
import math


# decorator to calculate duration
# taken by any function.
def calculate_time(func):
    # added arguments inside the wrapper,
    # if function takes any arguments,
    # can be added like this.
    def wrapper(*args, **kwargs):
        # storing time before function execution
        begin = time.time()

        func(*args, **kwargs)

        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)

    return wrapper


def factorial(num):
    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num))


# Decoration happens here.
factorial = calculate_time(factorial)
# calling the function.
factorial(10)


# --------------------------------------------------------------------------------------------------------------------
# decorator to calculate duration
# taken by any function.
def calculate_time(func):
    # added arguments inside the wrapper,
    # if function takes any arguments,
    # can be added like this.
    def wrapper(*args, **kwargs):
        # storing time before function execution
        begin = time.time()

        func(*args, **kwargs)

        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)

    return wrapper


# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):
    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num))


# calling the function.
factorial(10)
