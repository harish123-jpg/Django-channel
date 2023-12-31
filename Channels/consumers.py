from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class TestConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = "test_consumer"
        self.room_group_name = "test_consumer_group"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,  # Use room_group_name instead of room_name
            self.channel_name,
        )
        self.accept()
        self.send(text_data=json.dumps({'status': 'connesdasdadascted'}))

    def receive(self, text_data):
        self.send(text_data=json.dumps({'status': 'ssfsf'}))
        pass

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name,
        )