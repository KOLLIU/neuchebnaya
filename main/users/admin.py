from django.contrib import admin

from users.models import Prep


@admin.register(Prep)
class PrepAdmin(admin.ModelAdmin):
    pass
