# coding=utf-8

from flask import Flask
from flask_socketio import SocketIO

from config import SECRET_KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
socketio = SocketIO(app)
# When using with Vue-socketio, use the following to avoid cross-domain
# socketio = SocketIO(app , cors_allowed_origins="*")
