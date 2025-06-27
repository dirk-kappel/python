
# Decorator Factory
def timed(reps):
    def dec(fn):
        from time import perf_counter

        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                total_elapsed += (perf_counter() - start)
            avg_elapsed = total_elapsed / reps
            print(f"Avg Run time: {avg_elapsed:.6f}s ({reps} reps)")
            return result
        return inner
    return dec


def calc_fib_recurse(n):
    return 1 if n < 3 else calc_fib_recurse(n-2) + calc_fib_recurse(n-1)

@timed(5)
def fib(n):
    return calc_fib_recurse(n)

result = fib(28)
print(result)


# Creating a Decorator Factory
def dec_factory(a, b):
    print("Running decorator factory...")

    def dec(fn):
        print("Running dec...")

        def inner(*args, **kwargs):
            print("Running inner...")
            print(f"a={a}, b={b}")
            return fn(*args, **kwargs)

        return inner
    return dec

@dec_factory(10, 20)
def my_func():
    print("Running my_func...")

my_func()
