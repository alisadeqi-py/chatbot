# Generated by Django 4.2 on 2024-03-26 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_customers_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customers',
            old_name='intrested',
            new_name='car_intrested',
        ),
    ]