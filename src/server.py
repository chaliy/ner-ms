#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

from aiohttp import web
from aiohttp.web import Response
import aiohttp_cors
import sys, os
import json, yaml
from ner import extract, info

class JSONResponse(Response):
    """Serialize response to JSON with aiohttp.web"""

    def __init__(self, data, status=200,
                 reason=None, headers=None):
        body = json.dumps(data, ensure_ascii=False).encode('utf-8')

        super().__init__(body=body, status=status, reason=reason,
                         headers=headers, content_type='application/json')


SWAGGER_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'swagger.yaml')

__author__ = "Mike Chaliy"
__copyright__ = "Copyright 2016, Lang-UK"
__credits__ = ["Mike Chaliy", "Dmitry Chaplinsky", "Vsevolod Dyomkin"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Mike Chaliy"
__email__ = "mike@chaliy.name"

async def extract_handler(request):
    spec = await request.json()
    result = extract(spec)
    logging.info('Extracted entities %d from %d tokens', len(result['tokens']), len(result['entities']))
    return JSONResponse(result)

async def info_handler(request):
    return JSONResponse(info())

async def swagger_handler(request):
    with open(SWAGGER_PATH, 'r') as f:
        swagger = yaml.load(f.read())
        swagger['paths']['/']['post']['x-taskModel'] = os.environ['MITIE_MODEL_LANG']
        return JSONResponse(swagger)

app = web.Application()
app.router.add_route("POST", "/", extract_handler)
app.router.add_route("GET", "/", info_handler)
app.router.add_route("GET", "/swagger.json", swagger_handler)

# Enable CORS
cors = aiohttp_cors.setup(app, defaults={
    "*": aiohttp_cors.ResourceOptions(
            expose_headers="*",
            allow_headers="*",
        )
})

for route in list(app.router.routes()): cors.add(route)

if __name__ == "__main__":
    web.run_app(app)
