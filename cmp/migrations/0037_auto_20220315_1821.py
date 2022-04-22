# Generated by Django 2.2.13 on 2022-03-15 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmp', '0036_auto_20220315_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprasenc',
            name='clienteuniqueid',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='comprasenc',
            name='uso_factura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cmp.UsoFactura'),
        ),
    ]