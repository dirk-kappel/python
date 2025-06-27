# decorator_1.py
# An example of a timestamp decorator

import datetime
import time

def timestamp(func):
    def wrapper(*args):
        x = func(*args)
        print(x)
        print('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
    return wrapper
    
@timestamp
def add(a,b):
    return(a+b)
    
@timestamp
def square(a):
    return(a**2)

@timestamp
def exponential(a,b):
    return(a**b)
    
add(5,10)
time.sleep(1)
square(9)
time.sleep(2)
exponential(5,20)