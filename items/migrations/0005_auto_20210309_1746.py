# Generated by Django 2.1.5 on 2021-03-09 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_auto_20210308_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_Image',
            field=models.FileField(default='media/images/default.png', upload_to='images/'),
        ),
    ]
