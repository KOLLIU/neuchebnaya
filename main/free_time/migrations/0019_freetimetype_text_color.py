# Generated by Django 4.0 on 2024-10-31 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('free_time', '0018_remove_freetimeevent_weekdays_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='freetimetype',
            name='text_color',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Цвет текста'),
        ),
    ]
