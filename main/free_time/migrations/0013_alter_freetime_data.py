# Generated by Django 4.0 on 2024-10-28 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('free_time', '0012_remove_freetime_prep_freetime_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freetime',
            name='data',
            field=models.JSONField(verbose_name='Данные'),
        ),
    ]
