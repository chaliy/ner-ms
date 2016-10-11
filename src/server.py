#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, json, web
from ner import extract, info

__author__ = "Mike Chaliy"
__copyright__ = "Copyright 2016, Lang-UK"
__credits__ = ["Mike Chaliy", "Dmitry Chaplinsky", "Vsevolod Dyomkin"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Mike Chaliy"
__email__ = "mike@chaliy.name"


urls = { '/ner', 'NerHandler'}

class NerHandler:
    def POST(self):
        data = web.data()
        result = extract(data)

        return json.dumps(result)
    def GET(self):
        return json.dumps(info())

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
