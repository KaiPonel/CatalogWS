# Generated by Django 2.1.5 on 2021-03-25 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0011_item_neuesfeld'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='neuesFeld',
        ),
    ]
