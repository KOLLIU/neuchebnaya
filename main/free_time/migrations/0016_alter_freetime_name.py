# Generated by Django 4.0 on 2024-10-29 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('free_time', '0015_alter_freetime_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freetime',
            name='name',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Подпись'),
        ),
    ]