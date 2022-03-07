# Generated by Django 2.2.13 on 2022-02-26 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmp', '0033_auto_20220216_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprasdet',
            name='pedido',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='inv.Pedido'),
        ),
        migrations.AlterField(
            model_name='comprasenc',
            name='uso_factura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cmp.UsoFactura'),
        ),
    ]