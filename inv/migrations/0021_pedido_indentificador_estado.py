# Generated by Django 2.2.13 on 2021-09-27 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0020_pedido_folio_ingreso'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='indentificador_estado',
            field=models.CharField(default='1', max_length=20),
        ),
    ]