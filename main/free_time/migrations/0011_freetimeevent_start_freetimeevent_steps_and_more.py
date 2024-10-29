# Generated by Django 4.0 on 2024-10-28 19:39

from django.db import migrations, models
import django.db.models.deletion
import free_time.models


class Migration(migrations.Migration):

    dependencies = [
        ('free_time', '0010_alter_freetime_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='freetimeevent',
            name='start',
            field=models.CharField(default='0:00', max_length=5, verbose_name='Начальное время'),
        ),
        migrations.AddField(
            model_name='freetimeevent',
            name='steps',
            field=models.JSONField(default=free_time.models.get_event_time_steps, verbose_name='Варианты точности'),
        ),
        migrations.AddField(
            model_name='freetimeevent',
            name='stop',
            field=models.CharField(default='23:59', max_length=5, verbose_name='Конечное время'),
        ),
        migrations.AlterField(
            model_name='freetime',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='free_time.freetimeevent', verbose_name='Событие'),
        ),
    ]
