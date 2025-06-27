class A:
    counter = 0

    def __init__(self):
        A.counter += 1

    def __str__(self):
        return f'This class is testing how the class variable "counter" works.'
