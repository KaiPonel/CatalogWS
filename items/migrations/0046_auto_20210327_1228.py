# Generated by Django 3.1.7 on 2021-03-27 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0045_auto_20210327_1222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='item',
            name='color',
        ),
        migrations.RemoveField(
            model_name='item',
            name='description',
        ),
        migrations.RemoveField(
            model_name='item',
            name='glashuette',
        ),
        migrations.RemoveField(
            model_name='item',
            name='item_Image',
        ),
        migrations.RemoveField(
            model_name='item',
            name='kindOf',
        ),
        migrations.RemoveField(
            model_name='item',
            name='name',
        ),
        migrations.RemoveField(
            model_name='item',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='item',
            name='year',
        ),
    ]
