# Generated by Django 2.2.13 on 2021-08-21 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0005_auto_20210820_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='fecha_rechazo',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]