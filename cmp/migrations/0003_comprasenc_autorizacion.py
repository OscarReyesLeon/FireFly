# Generated by Django 2.2.13 on 2022-09-18 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmp', '0002_comprasenc_descuento2'),
    ]

    operations = [
        migrations.AddField(
            model_name='comprasenc',
            name='autorizacion',
            field=models.CharField(default='Autorización Pendiente', max_length=200),
        ),
    ]
