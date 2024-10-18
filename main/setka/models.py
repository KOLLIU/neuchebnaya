from django.contrib.auth.models import User
from django.db import models

from graf_quests.models import Game, ReadyClub
from users.models import Prep


# Create your models here.
class Club(models.Model):
    title = models.CharField(max_length=64)
    is_nav = models.BooleanField(default=False, verbose_name="Навигационная панель")
    responsible = models.ForeignKey(Prep, on_delete=models.CASCADE, null=True, blank=True,
                                    verbose_name="Ответственный")
    chat = models.CharField(max_length=256, default="", null=True, blank=True, verbose_name="Чат")
    doc = models.CharField(max_length=256, default="", null=True, blank=True, verbose_name="Док")
    ready = models.ForeignKey(ReadyClub, null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField(null=True, blank=True)
    chat_message_id = models.IntegerField(null=True, blank=True, verbose_name="id сообщения")

    class Meta:
        verbose_name = "Клуб"
        verbose_name_plural = "Клубы"

    def __str__(self):
        return self.title


week_days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
months = ["июл", "авг"]


class Day(models.Model):
    date = models.DateField(default=None, null=True, blank=True, verbose_name="День")
    week = models.IntegerField()
    day = models.IntegerField()

    game = models.OneToOneField(Game, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Игрушка",
                                related_name="day")
    club = models.OneToOneField(Club, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Клуб",
                                related_name="day")

    class Meta:
        verbose_name = "День"
        verbose_name_plural = "Дни"

    def __str__(self):
        return f" {week_days[self.day - 1]} {self.date.day} {months[self.date.month - 7]}"

    @property
    def return_week_day(self):
        return f"{week_days[self.day - 1]}"

    @property
    def return_date(self):
        return f"{self.date.day} {months[self.date.month - 7]}"


class File(models.Model):
    title = models.CharField(max_length=256, default="Название файла", verbose_name="Название файла")
    file = models.FileField(null=True, blank=True, verbose_name="Файл")

    def __str__(self):
        return self.title


class TaskTime(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["id"]


class Task(models.Model):
    task_time = models.ForeignKey(TaskTime, on_delete=models.PROTECT)
    title = models.CharField(max_length=256, null=True, blank=True)
    otv = models.ForeignKey(Prep, on_delete=models.PROTECT, null=True, blank=True )
    date = models.DateField()


class DoTask(models.Model):
    user = models.ForeignKey(Prep, on_delete=models.PROTECT, null=True, blank=True)
