# Generated by Django 3.1.7 on 2021-03-26 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0034_auto_20210326_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='color',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_Image',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(default='', max_length=120),
        ),
    ]
