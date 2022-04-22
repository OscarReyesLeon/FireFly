# Generated by Django 2.2.13 on 2022-03-15 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmp', '0035_auto_20220226_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='comprasenc',
            name='clienteuniqueid',
            field=models.CharField(default='ZienIyopDoQSJ2wkELqmJUxWCkSby4UGrWkyMDW6', max_length=100),
        ),
        migrations.AlterField(
            model_name='comprasdet',
            name='pedido',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inv.Pedido'),
        ),
        migrations.AlterField(
            model_name='comprasenc',
            name='uso_factura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cmp.UsoFactura'),
        ),
    ]