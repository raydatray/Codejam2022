import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.contrib.auth.models import User


class chatUser(WebsocketConsumer):
    def connect(self):
        currentUser = self.scope["user"]
        nextUsername = self.scope["url_route"]["kwargs"]["username"]
        nextUser = User.objects.get(username=nextUsername)
        self.room_group_name = "test"

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    def chat_message(self, event):
        message = event["message"]

        self.send(text_data=json.dumps({"type": "chat", "message": message}))
