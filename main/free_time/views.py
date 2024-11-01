from json import dumps, loads
from random import randint

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from free_time.models import FreeTime, FreeTimeType, FreeTimeEvent
from free_time.utils import weekdays_short, return_days, get_data_for_event_from_weekdays, get_times_from_start_and_stop


# Create your views here.
def index(request):
    event = FreeTimeEvent.objects.get(id=2)
    print(return_days(event.dates))
    return HttpResponse("success")


def get_event_free_time_without_user(request, event_slug):
    context = {"event_slug": event_slug}
    return render(request, "free_time/get_event_free_time_without_user.html", context=context)


def get_event_free_time_by_user(request, event_slug, name="-"):
    if not request.user.is_authenticated and name == "-":
        return redirect("get_event_free_time_without_user", event_slug)

    if name == "dont_show_free_time_modal":
        request.user.prep.free_time_modal = False
        request.user.save()

    event = FreeTimeEvent.objects.get(slug=event_slug)
    try:
        free_time_answer = FreeTime.objects.get(event=event, user=request.user)
    except:
        days = return_days(event.dates)
        data = {day["id"]: [str(event.default_free_time_type.id)] * 24 * 60 for day in days}
        if request.user.is_authenticated:
            free_time_answer = FreeTime(event=event, user=request.user, name=None, data=data)
        else:
            free_time_answer = FreeTime(event=event, user=None, name=name, data=data)
        free_time_answer.save()
    return redirect("free_time_by_slug", free_time_answer.slug)


def free_time_by_slug(request, free_time_slug):
    free_time = FreeTime.objects.get(slug=free_time_slug)
    event = free_time.event
    days = return_days(event.dates)
    steps = event.steps

    all_tables = []
    for step in steps:
        all_tables.append({
            "step": step,
            "times": get_times_from_start_and_stop(start=event.start, stop=event.stop, step=step)
        })

    data = free_time.data
    data = dumps(data, indent=None)

    free_time_types = FreeTimeType.objects.all().order_by("id")
    free_time_types_dict = {str(free_time_type.id): {"color": free_time_type.color,
                                                     "title": free_time_type.title} for free_time_type in
                            free_time_types}
    free_time_types_dict = dumps(free_time_types_dict, indent=None)

    context = {"days": days, "all_tables": all_tables,
               "free_time_types": free_time_types,
               "free_time_types_dict": free_time_types_dict,
               "data": data,
               "free_time": free_time,
               "event": event}
    return render(request, "free_time/get_free_time.html", context=context)


def set_free_time_by_slug(request, free_time_slug):
    free_time = FreeTime.objects.get(slug=free_time_slug)
    data = request.POST["data"].replace("\\", "")
    data = loads(data)
    free_time.data = data
    free_time.save()
    return HttpResponse("success")


def set_free_time_by_slug_with_weekdays(request, free_time_slug):
    if not request.user.is_authenticated:
        messages.error(request,
                       "Ошибка. Вы должны авторизоваться, чтобы получить данные из таблицы удобного времени по дням недели")
        return redirect("free_time_by_slug", free_time_slug)

    week_event = FreeTimeEvent.objects.get(id=1)
    try:
        free_time_weekdays = FreeTime.objects.get(user=request.user, event=week_event)
    except:
        messages.error(request, "Ошибка. Данный пользователь не заполнял таблицу удобного времени по дням недели")
        return redirect("free_time_by_slug", free_time_slug)

    free_time = FreeTime.objects.get(slug=free_time_slug)

    data = get_data_for_event_from_weekdays(free_time_weekdays, free_time)

    free_time.data = data
    free_time.save()

    return redirect("free_time_by_slug", free_time_slug)


def result_free_time_event_by_slug(request, event_slug, step="1:00"):
    event = FreeTimeEvent.objects.get(slug=event_slug)
    days = return_days(event.dates)
    times = []
    time_list = get_times_from_start_and_stop(start=event.start, stop=event.stop, step=step)
    for day in days:
        times.append({"id": day["id"], "title": day["title"], "times": time_list})

    free_times = FreeTime.objects.filter(event=event)

    prep_data = {}
    for free_time in free_times:
        name = f"{free_time.user.first_name} {free_time.user.last_name}"
        prep_data[name] = free_time.data
    # for name in range(100):
    #     prep_data[str(name)] = free_time.data

    free_time_types = FreeTimeType.objects.all().order_by("id")
    free_time_types_dict = {str(free_time_type.id): {"color": free_time_type.color,
                                                     "title": free_time_type.title} for free_time_type in
                            free_time_types}
    free_time_types_dict = dumps(free_time_types_dict, indent=None)

    context = {"times": times, "prep_data": prep_data,
               "prep_data_dict": dumps(prep_data, indent=None),
               "free_time_types": free_time_types,
               "free_time_types_dict": free_time_types_dict,
               "steps": event.steps, "active_step": step,
               "event": event
               }
    return render(request, "free_time/result_free_time_event.html", context=context)
