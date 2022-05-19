# Generated by Django 2.2.13 on 2022-05-18 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0047_auto_20220518_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artciulosestandarizados',
            name='descripcion',
            field=models.CharField(default=1, max_length=50, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='nombresrelacion',
            name='descripcion',
            field=models.CharField(default=1, max_length=50, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='nombresrelacion',
            name='relacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inv.Artciulosestandarizados'),
        ),
    ]
