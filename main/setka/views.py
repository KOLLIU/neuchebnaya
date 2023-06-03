import json

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from graf_quests.models import Game, ReadyGame, ReadyClub
from setka.models import Club, Day


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect("login")

    games = Game.objects.all()
    games = [game for game in games if len(Day.objects.filter(game=game)) == 0]

    clubs = Club.objects.all()
    clubs = [club for club in clubs if len(Day.objects.filter(club=club)) == 0]

    days = Day.objects.all()
    weeks = [[None] * 7 for i in range(4)]
    for day in days:
        weeks[day.week][day.day - 1] = day

    ready_games = ReadyGame.objects.all()
    ready_clubs = ReadyClub.objects.all()

    ready = [[ready_games[i], ready_clubs[i]] for i in range(len(ready_games))]

    context = {"games": games, "clubs": clubs, "weeks": weeks, "ready": ready}

    return render(request, "setka/index.html", context=context)


def set_event_day_by_id(request):
    if not request.user.is_authenticated:
        return redirect("login")

    event_id = request.POST["event_id"]
    day_id = request.POST["day_id"]

    is_game = event_id.startswith("game_")
    event_id = int(event_id[5:])

    event = Game.objects.get(id=event_id) if is_game else Club.objects.get(id=event_id)

    # Удаляем старый день
    if is_game:
        days = Day.objects.filter(game=event)
        if len(days) > 0:
            days[0].game = None
            days[0].save()
    else:
        days = Day.objects.filter(club=event)
        if len(days) > 0:
            days[0].club = None
            days[0].save()

    if day_id:
        day_id = int(day_id[4:])
        day = Day.objects.get(id=day_id)
        if is_game:
            day.game = event
        else:
            day.club = event
        day.save()

    return HttpResponse(json.dumps({"answer": "succes"}), content_type="application/json")


def event(request, event_type, event_id):
    event = Game.objects.get(id=event_id) if event_type == "game" else Club.objects.get(id=event_id)

    context = {"event": event, "event_type": event_type}

    return render(request, "setka/event.html", context=context)
