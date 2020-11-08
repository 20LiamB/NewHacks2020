from file_reader import *
from DataAnalysis import *
from Hackathon import *
from typing import List, TextIO
import operator
import matplotlib.pyplot as plt
import numpy as np


def returnFrequencies(textfile: TextIO):
    words = converter(textfile)
    fluff = converter('Stop Words.txt')
    dictionary = createDictionary(words)
    dropper = dropFluffWords(dictionary, fluff)
    sorted_x = dict(sorted(dropper.items(), key=operator.itemgetter(1), reverse = True) )
    print(sorted_x)

    res1 = dict(list(sorted_x.items())[:10:])

    return res1

d = np.random.laplace(loc=15, scale=3, size=500)

if __name__ == '__main__':
    myDictionary = returnFrequencies("message (1).txt")
    print(myDictionary)
    plt.bar(myDictionary.keys(), myDictionary.values())
    plt.xticks(rotation = 90)
    plt.show()