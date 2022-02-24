# Generated by Django 2.2.13 on 2022-02-17 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmp', '0024_auto_20220216_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='comprasenc',
            name='uso_factura',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='cmp.UsoFactura'),
        ),
        migrations.AlterField(
            model_name='comprasenc',
            name='no_factura',
            field=models.CharField(blank=True, default='Gastos en general (G03)', max_length=100, null=True),
        ),
    ]
