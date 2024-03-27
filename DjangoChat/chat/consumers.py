from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from chat.serializers import MessageSerializer
from chat.models import Message, Chat
from customer.models import Customers
import json

class ChatConsumer(WebsocketConsumer):

    def new_message(self, data):
        message = data['message']
        message_type = data['message_type']
        customer_id = data['customer']
        chat_id = data['chat_id']
        chat = Chat.objects.get(id=chat_id)
        customer = Customers.objects.get(id = customer_id)
        message_model = Message.objects.create(customer = customer, content = message,
                                               message_type = message_type, chat = chat)
        result = self.message_serializer(message_model)
        result = eval(result)
        self.send_to_chat_message(result["content"])

    def fetch_message(self, data):
        chat_id = data['chat_id']
        qs = Message.objects.filter(chat_id = chat_id).all()
        json_message = self.message_serializer(qs)
        json_message = json_message.replace('null', 'None')
        print(eval(json_message))
        content = {
            "message": eval(json_message),
            "command": "fetch_message"

        }
        self.chat_message(content)

    def message_serializer(self, qs):
        many = (lambda qs : True if (qs.__class__.__name__ == "QuerySet") else False)(qs)
        serialized = MessageSerializer(qs, many=many)
        content = json.dumps(serialized.data, ensure_ascii=False)
        return content

    def connect(self, room_name=None):

        self.room_name = room_name if room_name else self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name)

        self.accept()

    commands = {

        'new_message': new_message,
        'fetch_message': fetch_message
    }

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)


        command = text_data_json["command"]

        self.commands[command](self, text_data_json)

        # Send message to room group
    def send_to_chat_message(self, message):

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, dict(type = "chat.message", message = message, command = "new_message"))

    def chat_message(self, event):

        # Send message to WebSocket
        self.send(text_data=json.dumps(event))
