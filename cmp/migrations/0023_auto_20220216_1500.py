# Generated by Django 2.2.13 on 2022-02-16 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmp', '0022_auto_20220216_1457'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usofactura',
            old_name='uso_factura',
            new_name='descripcion',
        ),
    ]