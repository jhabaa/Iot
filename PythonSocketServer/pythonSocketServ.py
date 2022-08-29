"""
Server Websocket Python.
L'application .py qui reçoit les données du Broker les renvoi vers ce serveur,
source ./iot/bin/activate
"""

from aiohttp import web
import socketio
import json
sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)

async def index(request):
    """Serve the client-side application."""
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

@sio.event
def connect(sid, environ):
    print("connect ", sid)

@sio.on("my message")
async def chat_message(sid, data):
    print(sid, data)
    await sio.emit('my message', json.loads(data))

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

app.router.add_static('/static', 'static')
app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app)
