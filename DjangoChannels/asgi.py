import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from Channels.consumers import TestConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoChannels.settings')
django_asgi_application = get_asgi_application()

ws_patterns = [
    path('ws/test/', TestConsumer.as_asgi()),
]


application = ProtocolTypeRouter({
    "websocket": URLRouter(ws_patterns),
})
