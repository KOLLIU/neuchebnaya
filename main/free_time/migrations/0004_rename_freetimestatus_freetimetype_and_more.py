# Generated by Django 4.0 on 2024-10-28 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('free_time', '0003_freetimeevent_freetimestatus'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FreeTimeStatus',
            new_name='FreeTimeType',
        ),
        migrations.AlterModelOptions(
            name='freetimeevent',
            options={'verbose_name': 'Событие', 'verbose_name_plural': 'События'},
        ),
        migrations.AlterModelOptions(
            name='freetimetype',
            options={'verbose_name': 'Тип свободного времени', 'verbose_name_plural': 'Типы свободного времени'},
        ),
    ]
