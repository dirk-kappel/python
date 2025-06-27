# read_file.py
# This is testing the reading of files.

# Using read.
print("\nUsing read...")
with open("files/random_document.txt") as file:
    read = file.read()
print(type(read), read, end="\n")

# Using readline.
print("\nUsing readline...")
with open("files/random_document.txt") as file:
    readline_1 = file.readline()
    readline_2 = file.readline()
print("readline_1...")
print(type(readline_1), readline_1, end="\n")
print(readline_1.split("."))
print("readline_2...")
print(type(readline_2), readline_2, end="\n")

# Using readlines.
# This will retain the newline character at the end of the list element (if present).
print("\nUsing readlines...")
with open("files/random_document.txt") as file:
    readlines = file.readlines()
print(type(readlines), readlines, end="\n")

# Reading using read().splitlines().
# This will remove the newline character.
print("\nUsing read().splitlines()...")
with open("files/random_document.txt") as file:
    read_split = file.read().splitlines()
print(type(read_split), read_split, end="\n")

# Iterating through readlines.
print("\nIterating over readlines...")
for i in readlines:
    print(i)

# Iterating through read().splitlines().
print("\nIterating over read().splitlines()...")
for i in read_split:
    print(i)
