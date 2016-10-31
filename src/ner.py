import sys, os

parent = os.path.dirname(os.path.realpath(__file__))
sys.path.append(parent + '/../../MITIE/mitielib')

from mitie import *

MITIE_MODEL = os.environ['MITIE_MODEL']
print("Loading NER model " + MITIE_MODEL)
ner = named_entity_extractor(MITIE_MODEL)

def extract(spec):
    if spec is None: return {}
    tokens = spec.get('tokens', None)

    entities = ner.extract_entities(tokens)

    label = lambda range: " ".join(tokens[i] for i in range)

    return {
        "tokens": tokens,
        "entities": [
            { "score": e[2], "tag": e[1], "label": label(e[0]) } for e in entities
        ]
    }

def info():
    return {
        "lang": os.environ['MITIE_MODEL_LANG'],
        "tags": ner.get_possible_ner_tags()
    }
