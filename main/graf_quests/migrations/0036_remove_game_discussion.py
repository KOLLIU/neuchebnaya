# Generated by Django 4.0 on 2024-10-14 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graf_quests', '0035_alter_game_responsible'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='discussion',
        ),
    ]
