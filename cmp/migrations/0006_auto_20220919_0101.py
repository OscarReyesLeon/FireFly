# Generated by Django 2.2.13 on 2022-09-19 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmp', '0005_auto_20220918_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprasenc',
            name='autorizacion',
            field=models.CharField(default='OC: Editando - Incompleta', max_length=50),
        ),
    ]