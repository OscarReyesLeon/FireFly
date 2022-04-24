# Generated by Django 2.2.13 on 2022-04-22 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bita', '0006_auto_20220422_0616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='llavesenresguardo',
            name='recibo',
        ),
        migrations.AddField(
            model_name='ingresounidadpesada',
            name='motivo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='bita.MotivoIngresoUnidad'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='llavesenresguardo',
            name='involucrado',
            field=models.ForeignKey(default=1, help_text='Nombre de quien se recibe o entrega las llaves', on_delete=django.db.models.deletion.PROTECT, to='bita.OperadorPesado'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visitantes',
            name='nombre',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tanquesdiesel',
            name='nombre',
            field=models.CharField(help_text='Banco, Patio, Planta, ETC.', max_length=50, unique=True),
        ),
        migrations.CreateModel(
            name='ReciboEntrega',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('movimiento', models.CharField(help_text='recibo o entrega', max_length=7)),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Recibo o entrega',
            },
        ),
        migrations.AddField(
            model_name='llavesenresguardo',
            name='movimiento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='bita.ReciboEntrega'),
            preserve_default=False,
        ),
    ]