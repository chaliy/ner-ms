#!/usr/bin/python
# -*- coding: utf-8 -*-

from aiohttp import web
from aiohttp.web import Response
import json
from ner import extract, info

class JSONResponse(Response):
    """Serialize response to JSON with aiohttp.web"""

    def __init__(self, data, status=200,
                 reason=None, headers=None):
        body = json.dumps(data).encode('utf-8')

        super().__init__(body=body, status=status, reason=reason,
                         headers=headers, content_type='application/json')

__author__ = "Mike Chaliy"
__copyright__ = "Copyright 2016, Lang-UK"
__credits__ = ["Mike Chaliy", "Dmitry Chaplinsky", "Vsevolod Dyomkin"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Mike Chaliy"
__email__ = "mike@chaliy.name"

async def extract_handler(request):
    text = await request.text()
    return JSONResponse(extract(text))

async def info_handler(request):
    return JSONResponse(info())

app = web.Application()
app.router.add_route("POST", "/ner", extract_handler)
app.router.add_route("GET", "/ner", info_handler)

if __name__ == "__main__":
    web.run_app(app)
