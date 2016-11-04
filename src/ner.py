import sys, os
import logging

parent = os.path.dirname(os.path.realpath(__file__))
sys.path.append(parent + '/../../MITIE/mitielib')

from mitie import *

MITIE_MODEL = os.environ['MITIE_MODEL']
logging.info('Loading NER model %s', MITIE_MODEL)
ner = named_entity_extractor(MITIE_MODEL)
logging.info('NER model %s loaded', MITIE_MODEL)

def _entities(tokens):
    label = lambda range: " ".join(tokens[i] for i in range)
    entities = ner.extract_entities(tokens)

    return [
        { "score": e[2], "tag": e[1], "label": label(e[0]) } for e in entities
    ]

def _children(input, statistics):
    if len(input) is 0 or statistics["depth"] >= 100:
        return [];

    children = list(filter(lambda i: isinstance(i, list), input))
    tokens = list(filter(lambda i: not isinstance(i, list), input))

    entities = _entities(tokens)

    statistics["tokensCount"] += len(tokens)
    statistics["entitiesCount"] += len(entities)
    statistics["depth"] += 1

    for childInput in children:
        entities = entities + _children(childInput, statistics)

    return entities

def extract(spec):
    if spec is None: spec = {}
    tokens = spec.get('tokens', [])
    statistics = { "tokensCount": 0, "entitiesCount": 0, "depth": 0 }

    entities = _children(tokens, statistics)

    return {
        "entities": entities,
        "statistics": statistics
    }

def info():
    return {
        "lang": os.environ['MITIE_MODEL_LANG'],
        "tags": ner.get_possible_ner_tags()
    }
