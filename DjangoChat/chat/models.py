from django.db import models
from django.contrib.auth.models import User
from car.models import Car
from customer.models import Customers
# Create your models here.


class Chat(models.Model):
    dealer = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.OneToOneField(Customers, on_delete=models.CASCADE)
    ai_mode = models.BooleanField(default = True)

    def __str__(self):
        return f'{self.id}'


class Message(models.Model):

    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    content = models.TextField(max_length=150)
    message_type = models.CharField(max_length=25, blank = True, choices=[('Customer', 'C'), ('AI', 'A'), ('Dealer', 'D')])
    timestamp = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, blank = True, null = True)

    def __str__(self):

        return str(self.chat.dealer.username)
