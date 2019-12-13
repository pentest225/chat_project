# chat/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
import json
from . import models

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("##################### D I R ######################")
        await self.accept()

    async def disconnect(self, close_code):
        print("############## D I S C O  - S O K E T  ############")
        print("close_code",close_code)
        # Leave room group
        
#
    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message =text_data_json['message']
        print("############## R E C E V E - M E S S A G E ############")
        print(text_data)

        self.send(text_data=json.dumps({
            'message ':message
            
        }))