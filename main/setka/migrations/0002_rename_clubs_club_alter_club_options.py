# Generated by Django 4.0 on 2023-05-27 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('setka', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Clubs',
            new_name='Club',
        ),
        migrations.AlterModelOptions(
            name='club',
            options={'verbose_name': 'Клуб', 'verbose_name_plural': 'Клубы'},
        ),
    ]
