# Generated by Django 2.2.13 on 2021-09-27 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Idiomas',
            },
        ),
        migrations.CreateModel(
            name='Frase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(default='Anónimo', max_length=50)),
                ('frase', models.TextField(blank=True, null=True)),
                ('idioma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bases.Idioma')),
            ],
            options={
                'verbose_name_plural': 'Frases',
            },
        ),
    ]
