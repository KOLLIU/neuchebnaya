from json import dumps, loads

from django.http import HttpResponse
from django.shortcuts import render, redirect

from free_time.models import FreeTime, FreeTimeType, FreeTimeEvent
from free_time.utils import weekdays_short, return_days


# Create your views here.
def index(request):
    event = FreeTimeEvent.objects.get(id=2)
    print(return_days(event.dates))
    return HttpResponse("success")


def get_event_free_time_without_user(request, event_id):
    context = {"event_id": event_id}
    return render(request, "free_time/get_event_free_time_without_user.html", context=context)


def get_event_free_time_by_user(request, event_id, name="-"):
    if not request.user.is_authenticated and name == "-":
        return redirect("get_event_free_time_without_user", event_id)

    event = FreeTimeEvent.objects.get(id=event_id)
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

    start = int(event.start.split(":")[0]) * 60 + int(event.start.split(":")[1])
    stop = int(event.stop.split(":")[0]) * 60 + int(event.stop.split(":")[1])

    steps = event.steps

    all_tables = []
    for step in steps:
        s = int(step.split(":")[0]) * 60 + int(step.split(":")[1])
        all_tables.append({
            "step": step,
            "times": [f"{time // 60:0>2}:{time % 60:0>2}-{(time + s) // 60:0>2}:{(time + s) % 60:0>2}"
                      for time in range(start, stop, s)]
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


def set_free_time_by_slug_with_weekdays(request):
    pass
