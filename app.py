from aiohttp import web
import asyncio
import json
import base64
import logging
from os import mkdir, listdir, path
import re
import random
from sys import exit
"""
[
    {
        'text':'horrific halloween by ted bundy'
    },
    {   'text':'hyper realistic warp gate',
        'image_filename':'/path/to/image.jpg'
    },
    {
        'text':'too late to think of more'
    }
]
"""
APP_ROOT = path.dirname(path.abspath(__file__))
print(APP_ROOT)
DATA_DIR = path.join(APP_ROOT, "data/")
INDEX_FILE = path.join(APP_ROOT, 'index')
INDEX = list()
if not path.exists(INDEX_FILE):
    with open(INDEX_FILE, 'w+') as f:
        f.write(json.dumps([]))
else:
    with open(INDEX_FILE, 'r') as f:
        INDEX = json.loads(f.read())

if not path.exists(DATA_DIR):
    mkdir(DATA_DIR)

def index_consistency_update():
    # Remove file references to nonexistent files
    return True

logging.basicConfig(level=logging.DEBUG)


async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    text += "\n"
    return web.Response(text=text)


async def input_handler(request):
    data = await request.json()
    if 'text' not in data:
        return web.Response(reason="text field required", status=400)
    tmp_indx = dict()
    if 'image' in data:
        image_filename = str(random.randint(0,10000)).zfill(10) + ".gif"
        with open(image_filename, 'wb') as fo:
            image_data = base64.b64decode(data['image'])
            fo.write(image_data)
        tmp_indx['image_filename'] = path.join(DATA_DIR, image_filename)
    tmp_indx = data['text']
    app['index'].append(tmp_indx)
    resp = web.Response(
        status=200,
        reason="success"
    )
    return resp


async def list_uploads(request):
    return web.Response(status=200)

app = web.Application(client_max_size=4294967296)

app.add_routes([web.get('/', handle),
                web.get('/{name}', handle),
                web.post('/upload', input_handler),
                web.get('/list', list_uploads)])

if __name__ == '__main__':
    # Load available data first
    # load index file that looks like

    app['index'] = INDEX
    web.run_app(app)