# Generated by Django 3.2 on 2023-03-18 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0002_drivermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiclemodel',
            name='responsible',
            field=models.ForeignKey(blank=True, help_text='Chofer responsable del vehiculo (Opcional)', null=True, on_delete=django.db.models.deletion.SET_NULL, to='administration.drivermodel', verbose_name='Chofer responsable'),
        ),
    ]
