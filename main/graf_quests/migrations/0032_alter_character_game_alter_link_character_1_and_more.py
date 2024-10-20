# Generated by Django 4.1.4 on 2024-07-21 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('graf_quests', '0031_alter_character_prep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graf_quests.game', verbose_name='Игра'),
        ),
        migrations.AlterField(
            model_name='link',
            name='character_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='character_1', to='graf_quests.character', verbose_name='Первый персонаж'),
        ),
        migrations.AlterField(
            model_name='link',
            name='character_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='character_2', to='graf_quests.character', verbose_name='Второй персонаж'),
        ),
        migrations.AlterField(
            model_name='link',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graf_quests.game', verbose_name='Игра'),
        ),
        migrations.AlterField(
            model_name='quest',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graf_quests.game', verbose_name='Игра'),
        ),
    ]
