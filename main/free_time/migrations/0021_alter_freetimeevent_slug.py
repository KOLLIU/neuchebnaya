# Generated by Django 4.0 on 2024-10-31 21:56

from django.db import migrations, models
import free_time.models


class Migration(migrations.Migration):

    dependencies = [
        ('free_time', '0020_freetimeevent_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freetimeevent',
            name='slug',
            field=models.CharField(db_index=True, default=free_time.models.get_token_slug, editable=False, max_length=255, unique=True, verbose_name='URL'),
        ),
    ]
