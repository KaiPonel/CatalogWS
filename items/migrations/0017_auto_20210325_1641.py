# Generated by Django 3.1.7 on 2021-03-25 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0016_auto_20210325_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='Neues Feld',
        ),
        migrations.AlterField(
            model_name='item',
            name='artist',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='item',
            name='color',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
