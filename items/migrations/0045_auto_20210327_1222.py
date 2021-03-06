# Generated by Django 3.1.7 on 2021-03-27 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0044_auto_20210326_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='artist',
            field=models.CharField(blank=True, default=' ', max_length=100, verbose_name='Künstler'),
        ),
        migrations.AlterField(
            model_name='item',
            name='color',
            field=models.CharField(blank=True, default=' ', max_length=120, verbose_name='Farbe'),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.CharField(blank=True, default=' ', max_length=8000, verbose_name='Beschreibung'),
        ),
        migrations.AlterField(
            model_name='item',
            name='glashuette',
            field=models.CharField(blank=True, default=' ', max_length=100, verbose_name='Glashütte'),
        ),
        migrations.AlterField(
            model_name='item',
            name='kindOf',
            field=models.CharField(blank=True, default=' ', max_length=100, verbose_name='art'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(default=' ', max_length=100, verbose_name='Objektname'),
        ),
    ]
