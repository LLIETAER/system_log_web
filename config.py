# coding=utf-8
import os

SECRET_KEY = os.urandom(24)
LOG_FILE = '/var/log/nginx/access.log'  # Log file path
EVENT_NAME = 'response'  # socketio Event name
NAMESPACE = '/shell'  # socketio Name space
