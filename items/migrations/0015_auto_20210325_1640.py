# Generated by Django 3.1.7 on 2021-03-25 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0014_auto_20210325_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.CharField(default=None, max_length=120),
        ),
    ]
