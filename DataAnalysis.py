"""
data analysis
"""
import Hackathon
from typing import List


# take the list of frequencies and return the words with the biggest frequencies
# find length of frequencies list, return the words in the top half or quarter

# returns a list of the words with high frequencies
# assume that the list of frequencies is in order
def return_frequency_words(dictionary: dict) -> dict:
    length = len(dictionary)
    len_highf = length // 3  # assuming list of frequencies is in decreasing order
    hf_words = {}
    for i in dictionary:
        #hf_words.update(dictionary[i])
        hf_words[i] = dictionary[i]
    return hf_words

# return the sentences containing words from the highest frequency word list
#def return_hfsentences() -> ...:
    #...