# Generated by Django 3.0.5 on 2023-02-18 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tareas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100, verbose_name='Nombre de la rutina')),
                ('description', models.CharField(max_length=300, verbose_name='Descripción')),
            ],
        ),
    ]
