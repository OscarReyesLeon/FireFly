# Generated by Django 2.2.13 on 2021-09-11 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0017_auto_20210908_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='licenciacaduca',
            field=models.DateField(blank=True, null=True),
        ),
    ]
