def fib(n):
    print(f"Calculating fib({n})")
    return 1 if n <3 else fib(n-1) + fib(n-2)

class Fib:
    def __init__(self):
        self.cache = {1:1, 2:1}

    def fib(self, n):
        if n not in self.cache:
            print(f"Calculating fib({n})")
            self.cache[n] = self.fib(n-1) + self.fib(n-2)
        return self.cache[n]

f = Fib()
f.fib(10)

def fib_2():
    cache = {1:1, 2:1}

    def calc_fib(n):
        if n not in cache:
            print(f"Calculating fib({n})")
            cache[n] = calc_fib(n-1) + calc_fib(n-2)
        return cache[n]

    return calc_fib

f_2 = fib_2()
f_2(10)
f_2(11)


# Using decorators
def memoize(fn):
    cache = dict()

    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]

    return inner

@memoize
def fib(n):
    print(f"Calculating fib({n})")
    return 1 if n <3 else fib(n-1) + fib(n-2)

fib(10)
fib(11)

# Using memoize to cache results
@memoize
def fact(n):
    print(f"Calculating {n}!")
    return 1 if n < 2 else n * fact(n-1)

print(fact(8))
print(fact(6))

# Cache module
from functools import lru_cache


@lru_cache(maxsize=8)
def fib_3(n):
    print(f"Calculating fib({n})")
    return 1 if n <3 else fib_3(n-1) + fib_3(n-2)

print(fib_3(8))
print(fib_3(16))
print(fib_3(8))
