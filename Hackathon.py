import textrazor
from typing import List, Tuple, TextIO

def key_words(text: TextIO):
    text.readline()
    data = []
    for line in text:
        data.append(line.strip().split(',')) 
    
    textrazor.api_key = "cc40b9a7aad01b09dbc862b78e776c5b81b105a11f10939377d44bc3"
    client = textrazor.TextRazor(extractors=["entities", "topics"])
    client.set_cleanup_mode("cleanHTML")
    client.set_classifiers(["textrazor_newscodes"])
    response = client.analyze()

    for entity in response.entities():
        print (entity.id, entity.relevance_score, entity.confidence_score, 
               entity.freebase_types)