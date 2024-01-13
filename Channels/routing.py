from django.urls import path
from . import consumers

websocket_urlpatterms = [
    path('chat/', consumers.ChatConsumer.as_asgi())
]
