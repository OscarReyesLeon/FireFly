# Generated by Django 2.2.13 on 2022-02-26 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0042_empresa_horarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banco',
            name='descripcion',
            field=models.CharField(help_text='Bancos', max_length=20, unique=True),
        ),
    ]
