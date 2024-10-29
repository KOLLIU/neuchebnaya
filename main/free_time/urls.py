from django.urls import path

from free_time.views import index, get_event_free_time_by_user, free_time_by_slug, set_free_time_by_slug, \
    get_event_free_time_without_user

urlpatterns = [path("", index, name="free_time_main"),

               # Просто кто-то попытался открыть ивент
               path("get_event_free_time_by_user/<int:event_id>/<str:name>",
                    get_event_free_time_by_user,
                    name="get_event_free_time_by_user"),

               # Кто-то пытается войти в ивент по имени. Имя добавляем js кодом
               path("get_event_free_time_by_user/<int:event_id>",
                    get_event_free_time_by_user,
                    name="get_event_free_time_by_user_with_name"),

               # Сюда перекидывает, если не было авторизации пользователя
               path("get_event_free_time_without_user/<int:event_id>",
                    get_event_free_time_without_user,
                    name="get_event_free_time_without_user"),

               path("free_time_by_slug/<slug:free_time_slug>", free_time_by_slug, name="free_time_by_slug"),
               path("set_free_time_by_slug/<slug:free_time_slug>", set_free_time_by_slug, name="set_free_time_by_slug")]
