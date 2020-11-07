from file_reader import *
from DataAnalysis import *
from Hackathon import *
from typing import List, TextIO
import operator

def method1(textfile: TextIO):
    words = converter(textfile)
    fluff = converter('Stop Words.txt')
    dictionary = createDictionary(words)
    dropper = dropFluffWords(dictionary, fluff)
    sorted_x = sorted(dropper.items(), key=operator.itemgetter(1), reverse = True)    
    
    return return_frequency_words(sorted_x)