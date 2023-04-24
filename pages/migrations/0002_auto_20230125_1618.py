# Generated by Django 3.0.5 on 2023-01-25 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='order',
            field=models.IntegerField(default=1, verbose_name='Orden'),
        ),
        migrations.AlterField(
            model_name='page',
            name='visible',
            field=models.BooleanField(verbose_name='Visible?'),
        ),
    ]