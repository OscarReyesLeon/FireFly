# Generated by Django 2.2.13 on 2021-09-08 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0012_herramienta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='herramienta',
            name='descripcion',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='herramienta',
            name='motivo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='herramienta',
            name='tipo',
            field=models.CharField(max_length=100),
        ),
    ]