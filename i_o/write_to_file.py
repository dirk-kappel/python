# write_to_file.py
# Testing out how files are opened in write mode.

import create_random_text

with open("files/write_file.txt", "w") as file:
    # This will write the following sentences back to back. There is not a new line.
    file.write("This is writing the first sentence using file.write().")
    file.write("This is writing the second sentence using file.write().")
    file.write("\n")
    file.write("This is writing the third sentence using file.write() and adding the newline character at the end.\n")
    file.write("This is writing the fourth sentence using file.write().")


with open("files/write_lines_file.txt", "w") as file:
    # Testing write line
    # It does not add a new line between the writes.
    file.writelines("This is writing the first sentence using file.writelines().")
    file.writelines("This is writing the second sentence using file.writelines().")


write_list = [
    "First element of the write_list.",
    "Second element of the write_list.",
    "Third element of the write_list.",
    "Fourth element of the write_list.",
    "Fifth element of the write_list.",
    "Sixth element of the write_list.",
    ]


with open("files/write_lines_list.txt", "w") as file:
    # Testing writing lines by supplying a list.
    # It does not add a new line between the elements.
    file.writelines(write_list)


with open("files/write_lines_list_iterate.txt", "w") as file:
    # This is what will happen if you iterate over the write_list.
    for element in write_list:
        file.writelines(element)
        file.write("\n")


random_document = create_random_text.random_text.create_random_document()

with open("files/random_document.txt", "w") as file:
    # This will write the random document to a file. It looks like the newlines are honored.
    file.write(random_document)


with open("files/write_random_document.txt", "w") as file:
    # Testing writing lines by supplying a list.
    # It does not add a new line between the elements.
    file.writelines(random_document.splitlines())

with open("files/write_random_document_iterate.txt", "w") as file:
    # This is what will happen if you iterate over the write_list.
    for element in random_document.splitlines():
        file.writelines(element)
        file.write("\n")
