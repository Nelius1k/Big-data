# ...
# Revised by Parke Godfrey
# 2017-09-11

import sys
import re

# Function to check if a word is in stopwords-MySQL.txt
def is_word_in_file(word, filename):
    # Open the file in read mode
    with open(filename, 'r') as file:
        # Read all lines in the file
        for line in file:
            # Check if the word is in the current line
            if word in line.split():
                return True
    return False


my_dict = {}

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = filter(None, re.split('[\W+_]', line))
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # tab-delimited; the trivial word count is 1
        word_exists = is_word_in_file(word.lower(), 'stopwords-MySQL.txt')
        if word_exists is False:
            if word.lower() in my_dict:
                my_dict[word.lower()] += 1
            else:
                my_dict[word.lower()] = 1
            #print(my_dict[word.lower()])
            #print('%s\t%s' % (word.lower(), 1))
            
            
for word, count in my_dict.items():
    print(f'{word}\t{count}')
        