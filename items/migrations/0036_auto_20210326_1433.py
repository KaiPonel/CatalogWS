# Generated by Django 3.1.7 on 2021-03-26 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0035_auto_20210326_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_Image',
            field=models.FileField(default='images/default/default.png', upload_to='images/'),
        ),
    ]
