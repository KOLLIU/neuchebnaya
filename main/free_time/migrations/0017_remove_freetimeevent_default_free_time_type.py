# Generated by Django 4.0 on 2024-10-29 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('free_time', '0016_alter_freetime_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='freetimeevent',
            name='default_free_time_type',
        ),
    ]
