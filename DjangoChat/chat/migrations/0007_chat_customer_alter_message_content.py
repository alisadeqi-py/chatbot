# Generated by Django 4.2 on 2024-03-25 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customers_dealer'),
        ('chat', '0006_remove_message_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='customer.customers', unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(max_length=150),
        ),
    ]
