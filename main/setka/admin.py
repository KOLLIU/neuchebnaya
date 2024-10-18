from django.contrib import admin

from setka.models import Club, Day, File, TaskTime, Task, DoTask
from users.models import Prep


# Register your models here.
@admin.register(Club)
class ClubsAdmin(admin.ModelAdmin):
    list_display = ("title", "ready")

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'responsible':
            kwargs['queryset'] = Prep.objects.filter(tg_id__isnull=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    pass


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    pass


@admin.register(TaskTime)
class TaskTimeAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(DoTask)
class DoTaskAdmin(admin.ModelAdmin):
    pass
