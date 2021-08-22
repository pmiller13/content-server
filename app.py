import logging
from sys import getsizeof
from aiohttp import web


async def input_handler(request):
    data = await request.json()
    if 'text' not in data:
        return web.Response(status=400, reason="text field required")

    if 'image' not in data:
        logging.debug('image-less entry made')
        data['image'] = ""

    queue_entry = dict()

    queue_entry['text'] = data['text']
    queue_entry['image'] = data['image']

    app['download_queue'].append(queue_entry)

    logging.debug('queue_length=%s, queue_memory_usage=%s, entry_memory_usage=%s' % (
        len(app['download_queue']),
        getsizeof(app['download_queue']),
        getsizeof(queue_entry),
    ))
    return web.Response(status=200, reason="success")


async def list_queue(request):
    if len(app['download_queue']) == 0:
        return web.json_response([], status=200)
    return web.json_response(app['download_queue'], status=200)


async def pop_queue(request):
    if len(app['download_queue']) == 0:
        return web.json_response([], status=200)
    tmp = app['download_queue'].pop(0)
    return web.json_response(tmp, status=200)


logging.basicConfig(filename="app.log", level=logging.DEBUG)
app = web.Application(client_max_size=4294967296)
app['download_queue'] = list()
app.add_routes([web.post('/upload', input_handler),
                web.get('/download', pop_queue),
                web.get('/list', list_queue)])

web.run_app(app)
