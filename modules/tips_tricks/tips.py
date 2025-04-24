# --------------------------- 1 ---------------------------

# Ternary conditionals
 
condition = True

if condition:
    x = 1
else:
    x = 0

print(x)

# Faster Way to write in one line

x = 1 if condition else 0

print(x, end='\n\n')

# --------------------------- 2 ---------------------------

# Large numbers - hard to tell digits without counting

num1 = 10000000000
num2 = 100000000

total = num1 + num2

print(total)

# Use underscores as separators - doesn't effect the value
num1 = 10_000_000_000
num2 = 100_000_000

total = num1 + num2

print(total)

# Use String Formatting for the output
print(f'{total:,}', end='\n\n')

# --------------------------- 3 ---------------------------

# Opening and closing files

# Use a context manager to open file
with open('test.txt', 'r') as f:  # This way you don't need to manually close the file.
    file_contents = f.read()

words = file_contents.split(' ')
word_count = len(words)
print(word_count, end='\n\n')

# Use context managers any time you are opening and closing connections.

# --------------------------- 4 ---------------------------

# Use enumerate function when needing the index
names = ['Corey', 'Chris', 'Dave', 'Travis']

for index, name in enumerate(names):
    print(index, name)
print()

for index, name in enumerate(names, start=1):  # Change the start value
    print(index, name)
print()

# --------------------------- 5 ---------------------------

# Zip Function

names = ['Corey', 'Chris', 'Dave', 'Travis']
colors = ['Red', 'Blue', 'Green', 'Yellow']

# Loop over two lists at once using zip
for name, color in zip(names, colors):
    print(f"{name}'s favorite color is {color}")
print()

seasons = ['winter', 'summer', 'fall', 'spring']

# Three lists at once
for name, color, season in zip(names, colors, seasons):
    print(f"{name}'s favorite color is {color} and likes {season}")
print()

# Zip will stop when it comes to the shortest list.

# Zip is creating a tuple of the three values.
for value in zip(names, colors, seasons):
    print(value)
print()

# --------------------------- 6 ---------------------------

# Unpacking values
items = (1, 2)

a, b = (1, 2)

print(a)
print(b)

# If you don't need the second variable you can ignore it by
a, _ = (5, 6)
print(a, end='\n\n')

# If you are trying to unpack more values than variables
a, b, *c = (1, 2, 3, 4, 5)
print(a)
print(b)
print(c)

# Ignoring the remainder
a, b, *_ = (1, 2, 3, 4, 5)

print()

# --------------------------- 7 ---------------------------

# Getting and setting attributes

class Person():
    pass

person = Person()

# setattr to set attributes for the class

setattr(person, 'first', 'Dirk')

print(person.first)

# You can use variables when using setattr
my_key = 'last'
my_value = 'Kappel'

setattr(person, my_key, my_value)

print(person.last)

# getattr to get the attributes
last = getattr(person, my_key)
print(last, end='\n\n')


# --------------------------- 8 ---------------------------

# Inputting secret information using getpass

from getpass import getpass   # Using the getpass module to mask the password input

username = input('Username: ')
password = getpass('Password: ')
print('Logging in....')

# --------------------------- 9 ---------------------------

# Running python with the -m option

# -m : Module = will run the specific module after the -m and everything afterwards are arguments for the module.
# it will search sys.path for that module

# --------------------------- 10 --------------------------

# Learn more about objects

# help(module)

# Show only attributes and methods (abbreviated from help)
# dir(module)

# To determine if it is an attribute or method just run the following and look at the output
# re.match