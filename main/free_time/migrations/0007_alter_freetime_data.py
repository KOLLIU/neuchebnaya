# Generated by Django 4.0 on 2024-10-28 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('free_time', '0006_remove_freetime_date_remove_freetime_weekday_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freetime',
            name='data',
            field=models.JSONField(default=dict, verbose_name='Данные'),
        ),
    ]
