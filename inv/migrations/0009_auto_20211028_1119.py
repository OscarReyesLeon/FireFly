# Generated by Django 2.2.13 on 2021-10-28 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0008_auto_20211020_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='status2',
            field=models.CharField(default='Proximo', max_length=20),
        ),
    ]