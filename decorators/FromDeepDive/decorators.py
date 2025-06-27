# This is a decorator that will allow you to use the original function doc strings
from functools import wraps


def counter(fn):
    """Counts the number of times a function is run."""
    count = 0

    # Decorator inner with wraps and pass it functions
    # @wraps(fn)
    def inner(*args, **kwargs):
        """The inner closure."""
        nonlocal count
        count += 1
        print(f"Function {fn.__name__} was called {count} times.")
        return fn(*args, **kwargs)
    # This will also use the wraps decorator
    inner = wraps(fn)(inner)
    return inner


def add(a:int, b:int):
    """Returns sum of two numbers."""
    return a + b


# This will define the decorator
add = counter(add)

# This will run the function three times
print(add(12, 12))
print(add(30, 50))
print(add(99, 199))

def mult(a:int, b:int, c:int = 1):
    """Return the product of two or three numbers."""
    return a * b * c


# This will define the decorator
mult = counter(mult)

print(mult(3,4,5))
print(mult(99,99))
print(mult(5,9,12))

# This will define the decorator as well. Equal to my_func = counter(my_func)
@counter
def my_func(s:str, i:int) -> str:
    return s * i

print(my_func("hello", 3))
print(my_func("world", 5))
print(my_func("!", 30))

help(my_func)
