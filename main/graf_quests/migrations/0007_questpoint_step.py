# Generated by Django 4.1.1 on 2022-09-26 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graf_quests', '0006_quest_questpoint'),
    ]

    operations = [
        migrations.AddField(
            model_name='questpoint',
            name='step',
            field=models.IntegerField(default=1),
        ),
    ]
