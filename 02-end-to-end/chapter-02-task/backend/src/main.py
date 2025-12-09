import os
import socketio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# Create a Socket.IO server
sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins="*")
socket_app = socketio.ASGIApp(sio)

app = FastAPI()


@app.get("/api/health")
async def health_check():
    return {"status": "ok"}


# Mount the Socket.IO app
app.mount("/ws", socket_app)

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (Frontend)

# Create static directory if it doesn't exist (for local dev without build)
if not os.path.exists("static"):
    os.makedirs("static")

app.mount("/", StaticFiles(directory="static", html=True), name="static")


# Socket.IO event handlers
@sio.event
async def connect(sid, environ):
    print(f"Client connected: {sid}")


@sio.event
async def disconnect(sid):
    print(f"Client disconnected: {sid}")


@sio.event
async def join_room(sid, room_id):
    print(f"Client {sid} joined room {room_id}")
    sio.enter_room(sid, room_id)


@sio.event
async def code_change(sid, data):
    # data should contain 'room_id' and 'code'
    room_id = data.get("room_id")
    code = data.get("code")
    # Broadcast the code change to everyone else in the room
    await sio.emit("code_update", code, room=room_id, skip_sid=sid)
