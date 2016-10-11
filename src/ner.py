import sys, os

# Make sure you put the mitielib folder into the python search path.  There are
# a lot of ways to do this, here we do it programmatically with the following
# two statements:
parent = os.path.dirname(os.path.realpath(__file__))
sys.path.append(parent + '/../../MITIE/mitielib')

from mitie import *
from collections import defaultdict

print("Loading NER model...")
ner = named_entity_extractor('../uk_model.dat')
print("\nTags output by this NER model:", ner.get_possible_ner_tags())

def extract(text):
    tokens = tokenize(text)
    entities = ner.extract_entities(tokens)

    label = lambda range:  " ".join(tokens[i] for i in range)

    return {
        "text": text,
        "tokens": tokens,
        "entities": [
            { "score": e[2], "tag": e[1], "label": label } for e in entities
        ]
    }

def info():
    return {
        "tags": ner.get_possible_ner_tags()
    }
