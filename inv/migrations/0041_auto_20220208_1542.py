# Generated by Django 2.2.13 on 2022-02-08 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0040_empresa_urllogoempresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='divisa',
            field=models.CharField(default='MXN', max_length=3),
        ),
    ]