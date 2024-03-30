from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Message
from car.models import Car
from chat.chatbot.prompt import Prompt
from chat.chatbot.bot import chatbot
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
import re


@receiver(post_save, sender=Message)
def message_created(sender, instance, created, **kwargs):
    if created:
        print("New message created:")
        print(instance.message_type)
        if instance.chat.ai_mode is True and instance.message_type != 'AI':
            car_model = instance.chat.car.model
            car_color = instance.chat.car.color
            car_make = instance.chat.car.make
            car_description = instance.chat.car.description
            car_cost = instance.chat.car.price
            car_feature = Car.features
            user = instance.chat.dealer
            address = user.profile.address
            Open = user.profile.open
            close = user.profile.close
            phone = user.profile.phone
            name = user.profile.chat_bot_name
            customerName = instance.chat.customer.name
            dealerName = instance.chat.dealer.first_name
            dealerPhoneNumber = instance.chat.dealer.profile.phone
            customerGender = instance.chat.customer.gender
            carInfo = {
                "car_make": car_make,
                "car_color": car_color,
                "car_model": car_model,
                "car_cost": car_cost,
                "car_feature": car_feature,
                "car_description": car_description
            }
            bot_messages = []
            messages = Message.objects.filter(chat__id = instance.chat.id)
            for message in messages:
                content = message.content
                role = 'you' if message.message_type == 'AI' else 'customer'
                dic = {
                    'role': role,
                    'content': content
                }
                bot_messages.append(dic)
                dic = {}
            prompt = Prompt(name = name, carInfo = carInfo, dealerClose = close, customerName = customerName,
                   dealerPhoneNumber = dealerPhoneNumber, dealerOpen = Open, dealerAddress = address,
                   carCost = car_cost, chat_his = bot_messages)
            message = chatbot(prompt = prompt.temp)
            json_string = re.search(r'```json\n(.*?)\n```', message, re.DOTALL).group(1)
            print(json_data := json.loads(json_string))
            Message.objects.create(chat = instance.chat, content = json_data['outputMessage'], message_type = "AI")
            room_group_name = f'chat_{instance.chat.name}'
            print(room_group_name)
            channel_layer = get_channel_layer()
            text_data = {
                 'message':  json_data['outputMessage'],
                  "type": "chat.message",
             }
            async_to_sync(channel_layer.group_send)(room_group_name, text_data )
            print('sent to group')
        else:
            print('message was from AI')
