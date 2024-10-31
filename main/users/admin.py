from django.contrib import admin

from users.models import Prep


@admin.register(Prep)
class PrepAdmin(admin.ModelAdmin):
    search_fields = ("user__last_name", "user__first_name")
