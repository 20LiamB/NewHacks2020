"""
data analysis
"""
from Hackathon import getFrequencies
from Hackathon import createDictionary


# take the list of frequencies and return the words with the biggest frequencies
# find length of frequencies list, return the words in the top half or quarter

# returns a list of the words with high frequencies
# assume that the list of frequencies is in order
def return_frequency_words() -> List(str):
    length = len(getFrequencies)
    len_highf = length // 3  # assuming list of frequencies is in decreasing order
    hf_words = []
    for key in createDictionary.range(0, len_highf):
        hf_words.append(createDictionary[key])
    return hf_words

# return the sentences containing words from the highest frequency word list
def return_hfsentences() -> ...:
    ...