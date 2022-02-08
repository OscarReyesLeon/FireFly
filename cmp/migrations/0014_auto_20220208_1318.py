# Generated by Django 2.2.13 on 2022-02-08 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmp', '0013_auto_20220203_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprasenc',
            name='no_factura',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='clabeproveedor',
            field=models.BigIntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='cuentabanco',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
