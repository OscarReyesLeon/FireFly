# Generated by Django 2.2.13 on 2022-05-11 23:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DieselPiusiCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('stockinliter', models.FloatField(help_text='Stock en litros')),
                ('tanklevel', models.FloatField(help_text='MM')),
                ('tankporcentage', models.FloatField(help_text='Porcentaje')),
                ('date', models.CharField(max_length=100)),
                ('dispenseliters', models.FloatField(help_text='Litros despachados')),
                ('odometer', models.FloatField(help_text='Odometro')),
                ('presetvolume', models.FloatField(help_text='?')),
                ('vehicleplate', models.CharField(help_text='Placas', max_length=20)),
                ('drivername', models.CharField(help_text='Nombre conductor', max_length=50)),
                ('partnumber', models.IntegerField(help_text='Numero de parte en enero')),
                ('workorder', models.IntegerField(help_text='Numero de orden')),
                ('dispenseridentifier', models.CharField(help_text='Identificador de bomba', max_length=50)),
                ('time', models.CharField(help_text='texto', max_length=50)),
                ('dispensername', models.CharField(help_text='Nombre de la bomba', max_length=50)),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Carga de Diesel',
            },
        ),
    ]
