# Generated by Django 4.2 on 2024-03-29 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0012_remove_chat_chat_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]