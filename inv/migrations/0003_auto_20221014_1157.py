# Generated by Django 2.2.13 on 2022-10-14 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0002_auto_20220905_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='status',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='status2',
            field=models.CharField(default='Cotizando', max_length=20),
        ),
    ]