# Generated by Django 4.1.1 on 2022-10-01 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('graf_quests', '0016_quest_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='graf_quests.game', verbose_name='Игра'),
        ),
        migrations.AlterField(
            model_name='link',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='graf_quests.game', verbose_name='Игра'),
        ),
        migrations.AlterField(
            model_name='quest',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='graf_quests.game', verbose_name='Игра'),
        ),
        migrations.AlterField(
            model_name='questpoint',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='graf_quests.character', verbose_name='Персонаж'),
        ),
        migrations.AlterField(
            model_name='questpoint',
            name='description',
            field=models.TextField(default='', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='questpoint',
            name='quest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='graf_quests.quest', verbose_name='Квест'),
        ),
        migrations.AlterField(
            model_name='questpoint',
            name='step',
            field=models.IntegerField(verbose_name='Шаг'),
        ),
    ]
