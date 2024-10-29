# Generated by Django 4.0 on 2024-10-28 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('free_time', '0011_freetimeevent_start_freetimeevent_steps_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='freetime',
            name='prep',
        ),
        migrations.AddField(
            model_name='freetime',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]