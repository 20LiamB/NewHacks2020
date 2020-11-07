from typing import List, TextIO, Tuple
from Hackathon.py import getFrequencies, getWords, createDataSet
from file_reader.py import file_to_list


def comparison(file1: TextIO, file2: TextIO) -> List[str]:
    file_1 = open(file1)
    file_2 = open(file2)
    
    file_one = file_to_list(file1)
    file_two = file_to_list(file2)
    
    freq1 = getFrequencies(file_one)
    freq2 = getFrequencies(file_two)
    
    words1 = getWords(file_one)
    words2 = getWords(file_two)
    
    set1 = createDataSet(words1, freq1)
    set2 = createDataSet(words2, freq2)
    
    #open both files, convert files to lists, convert lists to dataset