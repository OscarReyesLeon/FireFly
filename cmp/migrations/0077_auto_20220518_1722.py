# Generated by Django 2.2.13 on 2022-05-18 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmp', '0076_auto_20220518_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprasenc',
            name='uso_factura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cmp.UsoFactura'),
        ),
    ]
