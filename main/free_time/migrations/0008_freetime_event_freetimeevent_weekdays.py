# Generated by Django 4.0 on 2024-10-28 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('free_time', '0007_alter_freetime_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='freetime',
            name='event',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='free_time.freetimeevent'),
        ),
        migrations.AddField(
            model_name='freetimeevent',
            name='weekdays',
            field=models.BooleanField(default=False, verbose_name='Регулярное время по неделям'),
        ),
    ]