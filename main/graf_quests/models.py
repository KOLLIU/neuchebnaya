from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class ReadyGame(models.Model):
    title = models.CharField(max_length=64)
    percent = models.IntegerField(default=0)
    color = models.CharField(max_length=8)

    class Meta:
        verbose_name = "Готовность игрушки"
        verbose_name_plural = "Готовности игрушек"
        ordering = ["percent"]

    def __str__(self):
        return f"{self.title}"


class ReadyClub(models.Model):
    title = models.CharField(max_length=64)
    percent = models.IntegerField(default=0)
    color = models.CharField(max_length=8)

    class Meta:
        verbose_name = "Готовность клуба",
        verbose_name_plural = "Готовности клубов"
        ordering = ["percent"]

    def __str__(self):
        return f"{self.title}"


class Game(models.Model):
    title = models.CharField(max_length=64, verbose_name="Название")
    is_nav = models.BooleanField(default=False, verbose_name="Навигационная панель")
    responsible = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                                    verbose_name="Ответственный")
    chat = models.CharField(max_length=256, default="", null=True, blank=True, verbose_name="Чат")
    discussion = models.CharField(max_length=256, default="", null=True, blank=True, verbose_name="Обсуждение")
    is_new = models.BooleanField(default=False, verbose_name="Новая")
    doc = models.CharField(max_length=256, default="", null=True, blank=True, verbose_name="Док")
    ready = models.ForeignKey(ReadyGame, null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Игрушка"
        verbose_name_plural = "Игрушки"

    def __str__(self):
        return self.title


class Character(models.Model):
    game = models.ForeignKey("Game", on_delete=models.PROTECT, verbose_name="Игра")
    name = models.CharField(max_length=64, verbose_name="Имя", null=True, blank=True)
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    role = models.CharField(max_length=256, blank=True, null=True, default="", verbose_name="Роль")
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    stuff = models.CharField(max_length=256, verbose_name="Стафф", default=None, null=True, blank=True)
    todo = models.CharField(max_length=256, verbose_name="Что доделать", default=None, null=True, blank=True)

    class Meta:
        verbose_name = "Персонаж"
        verbose_name_plural = "Персонажи"
        ordering = ["game", "role", "name"]

    def __str__(self):
        return f"({str(self.game)[:3:]}) {self.role + '' if self.role else ''}{self.name if self.name else ''}"

    def get_absolute_url(self):
        return reverse("character", kwargs={"character_id": self.pk})



class Link(models.Model):
    game = models.ForeignKey("Game", on_delete=models.PROTECT, verbose_name="Игра")
    character_1 = models.ForeignKey("Character", on_delete=models.PROTECT, verbose_name="Первый персонаж",
                                    related_name="character_1")
    character_2 = models.ForeignKey("Character", on_delete=models.PROTECT, verbose_name="Второй персонаж",
                                    related_name="character_2")
    text = models.TextField(verbose_name="Текст")

    class Meta:
        verbose_name = "Связь"
        verbose_name_plural = "Связи"

    def __str__(self):
        return f"({self.character_1.name}-{self.character_2.name}) - {self.text}"


class Quest(models.Model):
    game = models.ForeignKey("Game", on_delete=models.PROTECT, verbose_name="Игра")
    title = models.CharField(null=True, blank=True, max_length=256, verbose_name="Название")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")

    class Meta:
        verbose_name = "Квест"
        verbose_name_plural = "Квесты"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("get_quest", kwargs={"quest_id": self.pk})

    def read_points(self):
        self.points = QuestPoint.objects.filter(quest__id=self.id)
        return self


class QuestPoint(models.Model):
    quest = models.ForeignKey("Quest", on_delete=models.CASCADE, verbose_name="Квест")
    character = models.ForeignKey("Character", on_delete=models.CASCADE, verbose_name="Персонаж", null=True, blank=True)
    description = models.TextField(default="", verbose_name="Описание")
    step = models.FloatField(verbose_name="Шаг")
    stuff = models.CharField(max_length=256, verbose_name="Стафф", default=None, null=True, blank=True)
    todo = models.CharField(max_length=256, verbose_name="Что доделать", default=None, null=True, blank=True)

    class Meta:
        verbose_name = "Часть квеста"
        verbose_name_plural = "Части квестов"

    def __str__(self):
        return f"{self.quest} ({self.step})"

    def get_absolute_url(self):
        return reverse("get_quest", kwargs={"quest_id": self.quest.pk})
