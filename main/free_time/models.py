import random
import secrets

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from users.models import Prep


def get_token_slug():
    return secrets.token_urlsafe(32)


def get_event_time_steps():
    return ["0:05", "0:15", "0:30", "1:00"]


class FreeTimeType(models.Model):
    title = models.CharField(max_length=256, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    color = models.CharField(max_length=256, verbose_name="Цвет")
    weight = models.IntegerField(verbose_name="Вес")
    text_color = models.CharField(max_length=256, verbose_name="Цвет текста", null=True, blank=True)

    class Meta:
        verbose_name = "Тип свободного времени"
        verbose_name_plural = "Типы свободного времени"

    def __str__(self):
        return f"({self.id}) {self.title}"


class FreeTimeEvent(models.Model):
    title = models.CharField(max_length=256, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    dates = models.TextField(verbose_name="Даты")
    start = models.CharField(max_length=5, default="0:00", verbose_name="Начальное время")
    stop = models.CharField(max_length=5, default="23:59", verbose_name="Конечное время")
    steps = models.JSONField(default=get_event_time_steps, verbose_name="Варианты точности")
    default_free_time_type = models.ForeignKey(FreeTimeType, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=255,
                            default=get_token_slug,
                            unique=True, db_index=True, verbose_name="URL",
                            editable=False, blank=False)

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('result_free_time_event_by_slug', kwargs={'event_slug': self.slug, "step": "2:00"})


class FreeTime(models.Model):
    slug = models.SlugField(max_length=255, default=get_token_slug,
                            unique=True, db_index=True, verbose_name="URL",
                            editable=False, blank=False)
    data = models.JSONField(verbose_name="Данные")
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=256, blank=True, null=True, verbose_name="Подпись")
    event = models.ForeignKey(FreeTimeEvent, on_delete=models.CASCADE, verbose_name="Событие")

    class Meta:
        verbose_name = "Свободное время"
        verbose_name_plural = "Свободные времена"

    def __str__(self):
        return f"{self.user if self.user else self.name} - {self.event.title}"

    def get_absolute_url(self):
        return reverse('free_time_by_slug', kwargs={'free_time_slug': self.slug})
