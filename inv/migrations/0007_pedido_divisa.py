# Generated by Django 2.2.13 on 2021-10-18 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0006_auto_20211011_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='divisa',
            field=models.CharField(default='mxn', max_length=3),
        ),
    ]
