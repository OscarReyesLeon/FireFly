# Generated by Django 2.2.13 on 2022-05-05 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bita', '0013_auto_20220428_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destinosclientes',
            name='descripcion',
            field=models.CharField(help_text='Nombre Sucursal', max_length=50, unique=True),
        ),
    ]
