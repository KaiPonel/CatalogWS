# Generated by Django 3.1.7 on 2021-03-27 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0046_auto_20210327_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='artist',
            field=models.CharField(blank=True, default=' ', max_length=100, verbose_name='Künstler'),
        ),
        migrations.AddField(
            model_name='item',
            name='color',
            field=models.CharField(blank=True, default=' ', max_length=120, verbose_name='Farbe'),
        ),
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.CharField(blank=True, default=' ', max_length=8000, verbose_name='Beschreibung'),
        ),
        migrations.AddField(
            model_name='item',
            name='glashuette',
            field=models.CharField(blank=True, default=' ', max_length=100, verbose_name='Glashütte'),
        ),
        migrations.AddField(
            model_name='item',
            name='item_Image',
            field=models.FileField(default='images/default/default.png', upload_to='images/', verbose_name='Bild des Objekts'),
        ),
        migrations.AddField(
            model_name='item',
            name='kindOf',
            field=models.CharField(blank=True, default=' ', max_length=100, verbose_name='art'),
        ),
        migrations.AddField(
            model_name='item',
            name='name',
            field=models.CharField(default=' ', max_length=100, verbose_name='Objektname'),
        ),
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='item',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
