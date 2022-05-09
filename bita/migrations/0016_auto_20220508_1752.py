# Generated by Django 2.2.13 on 2022-05-08 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bita', '0015_motivoingresounidad_horasalida'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='motivoingresounidad',
            name='horasalida',
        ),
        migrations.AddField(
            model_name='ingresounidadpesada',
            name='ubicacion',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='bita.TanquesDiesel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ingresounidadpesada',
            name='fsalida',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
