# Generated by Django 4.1.1 on 2022-09-20 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graf_quests', '0004_alter_character_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Имя'),
        ),
    ]
