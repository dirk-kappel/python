

def timed(fn):
    from functools import wraps
    from time import perf_counter

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start

        args_ = [str(a) for a in args]
        kwargs_ = [f"{k} = {v}" for (k,v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ",".join(all_args)

        print(f"{fn.__name__}({args_str}) took {elapsed:.6f}s to run.")
        return result

    return inner

# Function the writes fibonacci numbers
def calc_recursive_fib(n):
    if n <= 2:
        return 1
    return calc_recursive_fib(n-1) + calc_recursive_fib(n-2)

# We add the decorated here because if we added it to the function above it would time each individual step of the function.
@timed
def fib_recursive(n):
    return calc_recursive_fib(n)

print(fib_recursive(6))
print(fib_recursive(20))
print(fib_recursive(35))


# You can also find fibonacci numbers using a loop
@timed
def fib_loop(n):
    fib_1 = 1
    fib_2 = 1
    for i in range(3, n+1):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    return fib_2

print(fib_loop(6))
print(fib_loop(20))
print(fib_loop(35))


"""
Reduction method.

n = 1
(1,0) --> (1,1) result t[0]

n = 2
(1,0) --> (1,1) --> (2,1) result t[0] = 2

n = 3
(1,0) --> (1,1) --> (2,1) --> (3,2) result t[0] = 3

n = 4
(1,0) --> (1,1) --> (2,1) --> (3,2) --> (5,3) result t[0] = 5
"""

from functools import reduce


@timed
def fib_reduce(n):
    initial = (1, 0)
    dummy = range(n-1)
    fib_n = reduce(lambda prev, n: (prev[0]+prev[1], prev[0])
                                    ,dummy
                                    ,initial)
    return fib_n[0]

print(fib_reduce(6))
print(fib_reduce(25))
print(fib_reduce(35))

