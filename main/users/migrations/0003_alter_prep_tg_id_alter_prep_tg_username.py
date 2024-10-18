# Generated by Django 4.0 on 2024-10-14 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_prep_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prep',
            name='tg_id',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='телеграм id'),
        ),
        migrations.AlterField(
            model_name='prep',
            name='tg_username',
            field=models.TextField(blank=True, max_length=128, null=True, verbose_name='телеграм username'),
        ),
    ]