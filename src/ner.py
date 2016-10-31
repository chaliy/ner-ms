import sys, os

parent = os.path.dirname(os.path.realpath(__file__))
sys.path.append(parent + '/../../MITIE/mitielib')

from mitie import *

print("Loading NER model...")
ner = named_entity_extractor('../uk_model.dat')

def extract(spec):
    if spec is None: return {}
    tokens = spec.get('tokens', None)

    entities = ner.extract_entities(tokens)

    label = lambda range:  " ".join(tokens[i] for i in range)

    return {
        "tokens": tokens,
        "entities": [
            { "score": e[2], "tag": e[1], "label": label(e[0]) } for e in entities
        ]
    }

def info():
    return {
        "tags": ner.get_possible_ner_tags()
    }
