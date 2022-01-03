# Generated by Django 2.2.13 on 2021-11-11 01:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0032_auto_20211110_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='apellido_materno',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='apellido_paterno',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='clabe_banco',
            field=models.BigIntegerField(unique=True, validators=[django.core.validators.MinValueValidator(111111111111111111), django.core.validators.MaxValueValidator(999999999999999999)]),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='contacto_emergencia',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='cuenta',
            field=models.BigIntegerField(unique=True, validators=[django.core.validators.MinValueValidator(10000000000), django.core.validators.MaxValueValidator(99999999999)]),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='nominaBanco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inv.Banco'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='nss',
            field=models.CharField(max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='puesto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inv.Puesto'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='rfc',
            field=models.CharField(max_length=13, unique=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='telefono_celular',
            field=models.BigIntegerField(unique=True, validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxValueValidator(9999999999)]),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='telefono_emergencia',
            field=models.BigIntegerField(validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxValueValidator(9999999999)]),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='telefono_fijo',
            field=models.BigIntegerField(validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxValueValidator(9999999999)]),
        ),
    ]