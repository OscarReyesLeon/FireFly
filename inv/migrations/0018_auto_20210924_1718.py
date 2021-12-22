# Generated by Django 2.2.13 on 2021-09-24 22:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0017_auto_20210924_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='precio_uni',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]
