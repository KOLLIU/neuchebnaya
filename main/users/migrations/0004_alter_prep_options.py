# Generated by Django 4.0 on 2024-10-14 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_prep_tg_id_alter_prep_tg_username'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prep',
            options={'ordering': ['tg_username'], 'verbose_name': 'Преподаватель', 'verbose_name_plural': 'Преподаватели'},
        ),
    ]