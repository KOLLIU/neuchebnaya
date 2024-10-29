from django.contrib import admin

from free_time.models import FreeTime, FreeTimeEvent, FreeTimeType


# Register your models here.
@admin.register(FreeTime)
class FreeTimeAdmin(admin.ModelAdmin):
    list_display = ("event", "name", "user")
    list_filter = ("event", )


@admin.register(FreeTimeType)
class FreeTimeTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(FreeTimeEvent)
class FreeTimeEventAdmin(admin.ModelAdmin):
    pass
