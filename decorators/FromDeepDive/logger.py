

def logged(fn):
    from datetime import datetime, timezone
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print(f"{run_dt}: called {fn.__name__}")
        return result

    return inner

@logged
def func_1():
    pass

@logged
def func_2():
    pass

func_1()
func_2()

def timed(fn):
    from functools import wraps
    from time import perf_counter

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        print(f"{fn.__name__} ran for {end-start:6f}s")
        return result

    return inner

@logged
@timed
# Equal to fact = logged(timed(fact))
# logged gets called first but time(fact) is passed into it
def fact(n):
    from functools import reduce
    from operator import mul

    return reduce(mul, range(1, n+1))

# Testing
print(fact(3))
print(fact(5))


def dec_1(fn):
    def inner():
        print("Running dec_1")
        return fn()
    return inner

def dec_2(fn):
    def inner():
        print("Running dec_2")
        return fn()
    return inner

@dec_1
@dec_2
@logged
@timed
def my_func():
    print("Running my_func")

my_func()
