import textrazor
from typing import List, Tuple, TextIO
from nltk.tokenize import sent_tokenize


#def file_to_list(text: TextIO):
    #f = open(text)
    #lst = f.readlines()
    #for line in range(len(lst)):
        #lst[line] = (lst[line].strip('\n')).lower()
        #lst[line] = (lst[line].split())
    #f.close()
    #return lst


#Converts file into seperate lines in a list
def convert_to_single_lines(textfile: TextIO):
    file = open(textfile)
    conversion = file.readlines()
    for line in range(len(conversion)):
        conversion[line] = (conversion[line].strip('\n').lower())
    token_text = sent_tokenize(', '.join(conversion))
    return token_text


#Converts file into individual words in a list
def converter(textfile2: TextIO):
    lst = []
    f = open(textfile2)
    for line in f:
        for word in line.split():
            lst.append(word.lower())
    return lst
