#!/usr/bin/env python
# -*-coding:utf-8 -*
import sys
import psycopg2

connection = psycopg2.connect(  user = "postgres",
                                password = "postgres",
                                host = "db",
                                port = "5432",
                                database = "proyecto")

for line in sys.stdin:
    docs = line.lower()
    arr = []
    i = 0

    # Split the document into name and document parts
    name, docs = docs.split('<splittername>')
    name, url = name.split()

    # Replace punctuation and numerical values with empty strings
    for char in [",", ".", '"', "'", "(", ")", "\\", ";", ":", "$1", "$", "&", "="]:
        docs = docs.replace(char, '')

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
    try:
     cursor = connection.cursor()
     for i in range(30):
      cursor.execute("INSERT INTO paginas (id, url) VALUES (%s, %s) ON CONFLICT (id) DO NOTHING", (name, url))
      connection.commit()

    except (Exception, psycopg2.Error) as error :
     print ("Error while connecting to PostgreSQL", error)
    finally:
         if(connection):
             cursor.close()
             connection.close()
      