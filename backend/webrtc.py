from application import app

from flask_socketio import SocketIO
from aiortc import RTCPeerConnection, RTCDataChannel, \
                   RTCIceCandidate, RTCSessionDescription

sio = SocketIO(app)

WebRTCConnections = {}

@sio.on("establish", namespace='/webrtc')
async def establish(sid, environ):
    WebRTCConnections = 

@sio.on("answer", namespace='/webrtc')
async def send_offer():
    pass

@sio.on("offer", namespace='/webrtc')
async def send_answer():
    pass

@sio.on("icecandidate", namespace='/webrtc')
async def add_icecandidate():
    pass

@sio.on("disconnect")
async def disconnect():
    pass

