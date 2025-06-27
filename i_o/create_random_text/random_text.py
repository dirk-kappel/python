# random_text.py
# This will test out creating random text.

import random


def lower_case():
    return chr(random.randint(97,122))

def create_random_word():
    word_length = random.randint(1,10)
    word = ""
    for _ in range(word_length):
        word += lower_case()
    return word

def create_random_sentence():
    sentence_length = random.randint(6,30)
    sentence = ""
    for i in range(sentence_length):
        # Account for capitalizing the starting of a sentence.
        if i == 0:
            sentence += create_random_word().capitalize() + " "
            continue
        sentence += create_random_word()
        # Add a space in between words.
        if i < sentence_length-1:
            sentence += " "
        # If we are at the end of the sentence then add a period.
        else:
            sentence += "."
    return sentence

def create_random_paragraph():
    paragraph_length = random.randint(2,5)
    paragraph = ""
    for i in range(paragraph_length):
        paragraph += create_random_sentence()
        if i < paragraph_length-1:
            paragraph += " "
    return paragraph

def create_random_document():
    document_length = random.randint(3,7)
    document = ""
    for i in range(document_length):
        document += create_random_paragraph()
        # If we are at the end of the paragraph then add a newline.
        if i < document_length-1:
            document += "\n"
    return document

if __name__ == "__main__":
    document = create_random_document()
    print(document)
    doc_list = document.split("\n")
    print(doc_list)
