# Generated by Django 4.1.4 on 2023-07-23 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setka', '0010_tasktime_task_dotask'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasktime',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='file',
            name='title',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
