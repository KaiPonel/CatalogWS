# Generated by Django 3.1.7 on 2021-03-25 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0017_auto_20210325_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='Neues Feld',
            field=models.CharField(default=None, max_length=120),
        ),
        migrations.AlterField(
            model_name='item',
            name='artist',
            field=models.CharField(default=None, max_length=120),
        ),
        migrations.AlterField(
            model_name='item',
            name='color',
            field=models.CharField(default=None, max_length=120),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(default=None, max_length=120),
        ),
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.CharField(default=None),
        ),
    ]
