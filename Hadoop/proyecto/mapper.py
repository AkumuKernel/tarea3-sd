#!/usr/bin/env python
# -*-coding:utf-8 -*
import sys

for line in sys.stdin:
    docs = line.lower()
    arr = []

    # Replace punctuation and numerical values with empty strings
    for char in [",", ".", '"', "'", "(", ")", "\\", ";", ":", "$1", "$", "&", "="]:
        docs = docs.replace(char, '')

    # Split the document into name and document parts
    name, docs = docs.split('<splittername>')
    name, url = name.split()

    # Process each word in the document
    for word in docs.split():
        # Check if the word is a letter
        if not word.isalpha():
            # Skip the word
            continue

        # Add the processed word to the array
        arr.append('{}\t{}\t{}'.format(word, name, 1))

    # Sort and print the processed words
    for i in sorted(arr):
        print(i)