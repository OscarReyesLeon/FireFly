# Generated by Django 2.2.13 on 2021-09-25 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0018_auto_20210924_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='articulo',
            field=models.CharField(max_length=35),
        ),
    ]
