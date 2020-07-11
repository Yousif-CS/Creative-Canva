from application import app

import socketio
import aiortc
# create a Socket.IO server
sio = socketio.AsyncServer()

sio.attach(app)

@sio.event
async def connect(sid, environ):
    pass

@sio.on("answer")
async def send_offer():
    pass

@sio.on("offer")
async def send_answer():
    pass

@sio.on("icecandidate")
async def add_icecandidate():
    pass

@sio.event
async def disconnect():
    pass

