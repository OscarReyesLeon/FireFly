# Generated by Django 2.2.13 on 2022-10-17 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0004_auto_20221017_0120'),
        ('cmp', '0006_auto_20220919_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='comprasenc',
            name='autorizado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='comprasenc',
            name='autorizante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='inv.Pedido'),
        ),
        migrations.AddField(
            model_name='comprasenc',
            name='compras',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='comprasenc',
            name='cxp',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='comprasenc',
            name='io',
            field=models.IntegerField(default=1),
        ),
    ]