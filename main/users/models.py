from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Prep(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь", null=True, blank=True)
    tg_username = models.TextField(max_length=128, verbose_name="телеграм username", null=True, blank=True)
    tg_id = models.BigIntegerField(verbose_name="телеграм id", null=True, blank=True)

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"
        ordering = ['user__last_name']

    def __str__(self):
        return f"{self.user.last_name + '. ' if self.user.last_name else ''}{self.user.first_name + ' ' if self.user.first_name else ''}({self.tg_username})"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Prep.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.prep.save()
