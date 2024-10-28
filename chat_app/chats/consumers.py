import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    async def connect(self):
        self.connect()
    async def disconnect(self, code):
        pass
    async def receive(self, text_data=None):
        text_data_json= json.loads(text_data)
        message=text_data_json['message']
        self.send(text_data=json.dumps({"message":message}))