# Generated by Django 2.2.13 on 2021-09-27 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0019_auto_20210925_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='folio_ingreso',
            field=models.CharField(default='--', max_length=20),
        ),
    ]
