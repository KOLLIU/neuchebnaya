from django.contrib import admin

from setka.models import Club, Day


# Register your models here.
@admin.register(Club)
class ClubsAdmin(admin.ModelAdmin):
    list_display = ("title", "ready")


@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    pass
