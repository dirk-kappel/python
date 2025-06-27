
# Decorator Factory using a class.
class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, fn):
        def inner(*args, **kwargs):
            print(f"Decorated function called: a = {self.a}, b= {self.b}")
            return fn(*args, **kwargs)
        return inner

@MyClass(100, 200)
def my_func(s):
    print(f"Hello {s}")

my_func("World!")
