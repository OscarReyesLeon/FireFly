# Generated by Django 2.2.13 on 2022-02-04 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0038_auto_20220203_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='rfcempresa',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
