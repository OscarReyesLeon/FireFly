# Generated by Django 2.2.13 on 2022-02-09 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0041_auto_20220208_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='horarios',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]