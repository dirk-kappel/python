class A:
    counter = 0

    def __init__(self, number):
        self.number = number
        A.counter += 1

    def __str__(self):
        return f'This class is testing how the class variable "counter" works.'

    def __add__(self, other_object):
        print('Using the defined __add__ function of this class.')
        return self.number + other_object.number

    def __getattr__(self, attribute):
        return f'{attribute} does not exist.'