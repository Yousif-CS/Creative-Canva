from app import app

from flask_socketio import SocketIO, send, emit
from aiortc import RTCPeerConnection, RTCDataChannel, \
                   RTCIceCandidate, RTCSessionDescription

sio = SocketIO(app)

WebRTCConnections = {}



@sio.on("establish", namespace='/webrtc')
async def establish(sid, environ):
    #create a webrtc connection
    WebRTCConnections[sid] = RTCPeerConnection()
    sdpOffer = WebRTCConnections[sid].createOffer()
    emit("offer", sdpOffer, namespace='/webrtc',
    callback=lambda: WebRTCConnections[sid].setLocalDescription(sdpOffer))


@sio.on("answer", namespace='/webrtc')
async def handle_answer(sidSrc, sidDest, answer):
    #emit an offer
    sio.emit("answer", answer, room=sidDest)
    

@sio.on("offer", namespace='/webrtc')
async def handle_offer(sidSrc, sidDest, offer):
    sio.emit("offer", offer, room=sidDest)

@sio.on("icecandidate", namespace='/webrtc')
async def add_icecandidate(sidSrc, sidDest, icecandidate):
    sio.emit("icecandidate", icecandidate, room=sidDest)

@sio.on("disconnect")
async def disconnect():
    pass

