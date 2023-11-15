from operator import itemgetter
import sys

current_word = None
current_documents = set()
word = None

for line in sys.stdin:
    line = line.strip()
    word, document_id = line.split('\t', 1)

    if current_word == word:
        current_documents.add(document_id)
    else:
        if current_word:
            # Output the inverted index
            print '%s\t%s' % (current_word, ','.join(current_documents))
        current_documents = {document_id}
        current_word = word

# Output the last inverted index if needed
if current_word == word:
    print '%s\t%s' % (current_word, ','.join(current_documents))
