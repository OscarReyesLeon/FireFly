# Generated by Django 2.2.13 on 2022-05-18 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0046_auto_20220518_1723'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artciulosestandarizados',
            old_name='descripción',
            new_name='descripcion',
        ),
        migrations.AlterField(
            model_name='nombresrelacion',
            name='relacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inv.Artciulosestandarizados'),
        ),
    ]
