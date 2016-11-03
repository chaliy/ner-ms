import sys, os
import logging

parent = os.path.dirname(os.path.realpath(__file__))
sys.path.append(parent + '/../../MITIE/mitielib')

from mitie import *

MITIE_MODEL = os.environ['MITIE_MODEL']
logging.info('Loading NER model %s', MITIE_MODEL)
ner = named_entity_extractor(MITIE_MODEL)
logging.info('NER model %s loaded', MITIE_MODEL)

def extract(spec):
    if spec is None: spec = {}
    tokens = spec.get('tokens', [])

    entities = ner.extract_entities(tokens)

    label = lambda range: " ".join(tokens[i] for i in range)

    return {
        "entities": [
            { "score": e[2], "tag": e[1], "label": label(e[0]) } for e in entities
        ],
        "statistics": {
            "tokensCount": len(tokens),
            "entitiesCount": len(entities),
        }
    }

def info():
    return {
        "lang": os.environ['MITIE_MODEL_LANG'],
        "tags": ner.get_possible_ner_tags()
    }
