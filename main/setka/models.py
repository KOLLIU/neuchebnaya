from django.contrib.auth.models import User
from django.db import models

from graf_quests.models import Game, ReadyClub


# Create your models here.
class Club(models.Model):
    title = models.CharField(max_length=64)
    is_nav = models.BooleanField(default=False, verbose_name="Навигационная панель")
    responsible = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                                    verbose_name="Ответственный")
    chat = models.CharField(max_length=256, default="", null=True, blank=True, verbose_name="Чат")
    discussion = models.CharField(max_length=256, default="", null=True, blank=True, verbose_name="Обсуждение")
    doc = models.CharField(max_length=256, default="", null=True, blank=True, verbose_name="Док")
    ready = models.ForeignKey(ReadyClub, null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField(null=True, blank=True)

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
