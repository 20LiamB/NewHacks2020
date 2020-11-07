
import textrazor
import pandas as pd
from typing import List, Tuple, TextIO
from pandas import DataFrame

# def key_words(text: TextIO):
#     text.readline()
#     data = []
#     for line in text:
#         data.append(line.strip().split(','))
#
#     textrazor.api_key = "cc40b9a7aad01b09dbc862b78e776c5b81b105a11f10939377d44bc3"
#     client = textrazor.TextRazor(extractors=["entities", "topics"])
#     client.set_cleanup_mode("cleanHTML")
#     client.set_classifiers(["textrazor_newscodes"])
#     response = client.analyze()
#
#     for entity in response.entities():
#         print (entity.id, entity.relevance_score, entity.confidence_score,
#                entity.freebase_types)


frequencies = []
wordList = []

# creates a dictionary from the words and frequencies we extracted
# simultaneously creates a list of frequencies and single instances of words
def createDictionary(words: List[str]) -> dict:

    for i in range(len(words)):
        if wordList.count(words[i]) == 0:
            frequencies.append(words.count(words[i]))
            wordList.append(words[i])

    zip_iterator = zip(wordList, frequencies)

    newDict = dict(zip_iterator)

    return newDict


# # creates a data set from the words and frequencies we extracted
# def createDataSet(words: List[str], frequencies: List[int]):
#
#     dataSet = {'Word': words, 'Frequency': frequencies}
#
#     df = pd.DataFrame(dataSet, columns=['Word', 'Frequency'])
#
#     print(df)
#
#     return df


# # removes the rows from the data frame that contain fluff words
# def dropFluffWords(df: DataFrame, fluff: List[str]):
#     for i in range(len(fluff)):
#         df = df[df.Word != fluff[i]] #not a big fan of this because it seems like an expensive operation
#         #df.drop(fluff[i])
#
#     return df

# removes the rows from the dictionary that contain fluff words
def dropFluffWords(newDict: dict, fluff: List[str]) -> dict:
    for i in range(len(fluff)):
        del newDict[fluff[i]]
        #newDict.del(fluff[i])

    return newDict

if __name__ == '__main__':
    wordsss = ["poop", "sock", "poop", "sock", "poop", "kobi", "drav", "liam", "max", "max", "max", "max", "max is lame", "max is a poopoo"]
    fluff = ["poop", "max"]

    df = createDictionary(wordsss)

    df = dropFluffWords(df, fluff)

    print(df)

