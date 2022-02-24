# Generated by Django 2.2.13 on 2022-02-17 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmp', '0025_auto_20220216_1851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comprasenc',
            name='uso_factura',
        ),
        migrations.AlterField(
            model_name='comprasenc',
            name='no_factura',
            field=models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.PROTECT, to='cmp.UsoFactura'),
        ),
    ]
