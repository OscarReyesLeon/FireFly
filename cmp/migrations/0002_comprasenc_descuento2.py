# Generated by Django 2.2.13 on 2022-07-10 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comprasenc',
            name='descuento2',
            field=models.FloatField(default=0),
        ),
    ]