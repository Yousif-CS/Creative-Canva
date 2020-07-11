import socketio
import aiortc
# create a Socket.IO server
sio = socketio.AsyncServer()

# wrap with ASGI application
app = socketio.ASGIApp(sio)

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

