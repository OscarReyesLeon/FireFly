# Generated by Django 2.2.13 on 2022-09-05 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='indentificador_estado',
            field=models.CharField(default='1', max_length=20),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='status',
            field=models.CharField(default='X-Autorizar', max_length=20),
        ),
    ]