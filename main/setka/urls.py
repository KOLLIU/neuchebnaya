from django.urls import path

from .views import index, set_event_day_by_id, event, get_files

urlpatterns = [path("", index, name="main_page_url"),
               path("set_event_day_by_id", set_event_day_by_id),
               path("event/<str:event_type>/<int:event_id>", event, name="event"),
               path("get_files", get_files, name="get_files")]
