# Generated by Django 4.1.4 on 2023-07-22 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graf_quests', '0029_alter_character_options_character_stuff_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='prep',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
