# Generated by Django 2.2.13 on 2022-04-22 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmp', '0055_auto_20220422_0621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprasenc',
            name='uso_factura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cmp.UsoFactura'),
        ),
    ]
