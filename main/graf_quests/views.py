import json

from django.db.models import Q
from django.forms import modelformset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect

from graf_quests.forms import CharacterForm, QuestForm, QuestPointForm
from graf_quests.models import Character, Link, QuestPoint, Quest, Game
from main.settings import BASE_DIR, DEBUG


def index(request, game_id=1):
    if not request.user.is_authenticated:
        return redirect("login")

    characters = Character.objects.filter(game__id=game_id)

    characters_dict = {}
    for character in characters:
        start_quests = list(QuestPoint.objects.filter(character=character, step=0))
        in_quests = list(QuestPoint.objects.filter(character=character))
        characters_dict[character.id] = {"character": character,
                                         "start_quests": len(start_quests),
                                         "in_quests": len(in_quests)}

    links = Link.objects.filter(game__id=game_id)

    context = {"characters": characters_dict, "links": links, "game_id": game_id}

    return render(request, "graf_quests/index.html", context=context)


def set_character_info(character):
    character_id = character.id

    quest_points = list(QuestPoint.objects.filter(character=character))
    quest_points = sorted(quest_points, key=lambda x: x.step)
    quests_start_id = set([x.quest.id for x in quest_points if x.step == 0])
    quests_all_id = set([x.quest.id for x in quest_points])
    quests_all_id -= quests_start_id

    start_quests = [Quest.objects.get(id=quest_id) for quest_id in quests_start_id]
    for quest in start_quests:
        quest.character = character
    all_quests = [Quest.objects.get(id=quest_id) for quest_id in quests_all_id]
    for quest in all_quests:
        quest.character = character

    character.start_quests = start_quests
    character.is_start = len(start_quests) > 0
    character.all_quests = all_quests
    character.is_all = len(all_quests) > 0

    links = Link.objects.filter(Q(character_1=character_id) | Q(character_2=character_id))
    for link in links:
        link.pair = link.character_1 if link.character_1 != character else link.character_2
    character.links = links


def get_character(request, character_id):
    if not request.user.is_authenticated:
        return redirect("login")

    character = Character.objects.get(id=character_id)

    if request.method == "POST":
        form = CharacterForm(request.POST, instance=character)
        if form.is_valid():
            form.save()
            # data = form.cleaned_data
            return redirect("character", character_id=character_id)
    else:
        form = CharacterForm(instance=character)
        set_character_info(character)

        context = {"character": character, "form": form}

        return render(request, "graf_quests/character.html", context=context)


def get_all_characters(request, game_id):
    characters = list(Character.objects.filter(game__id=game_id))
    for character in characters:
        set_character_info(character)
    context = {"characters": characters}
    return render(request, "graf_quests/characters.html", context=context)


def create_character(request, game_id):
    game = Game.objects.get(id=game_id)
    character = Character(game=game)
    character.save()
    return redirect("character", character.id)


def get_quest(request, quest_id):
    if not request.user.is_authenticated:
        return redirect("login")

    quest = Quest.objects.get(id=quest_id)
    quest_point_formset_factory = modelformset_factory(model=QuestPoint, form=QuestPointForm, extra=1)
    quest_points = QuestPoint.objects.filter(quest__id=quest_id).order_by("step")

    if request.method == "POST":
        formset = quest_point_formset_factory(request.POST, request.FILES,
                                              queryset=quest_points)

        form = QuestForm(request.POST, instance=quest)
        if form.is_valid():
            form.save()

        if formset.is_valid():
            for form in formset:
                if form.is_valid():
                    point = form.save(commit=False)
                    try:
                        point.character
                        point.quest = quest
                        point.save()
                    except:
                        continue
        elif DEBUG:
            return HttpResponse(formset)

        return redirect("quest", quest_id=quest_id)

    else:
        quest_form = QuestForm(instance=quest)

        formset = quest_point_formset_factory(queryset=quest_points)

        points = []
        for i, form in enumerate(formset):
            point_id = quest_points[i].id if i < len(quest_points) else 999999
            character = quest_points[i].character if i < len(quest_points) else None
            points.append({"form": form, "id": point_id, "character": character})

        points_table = {}
        for point in quest_points:
            points_table[int(point.step)] = points_table.get(int(point.step), []) + [point]

        points_table = [points_table[key] for key in sorted(points_table.keys())]
        max_points_len = max([len(points_list) for points_list in points_table])
        max_points_text_len = max([max([len(point.description) for point in points_list])
                                   for points_list in points_table])
        points_width = 100 / (max_points_len + 1)

        points_font_size = points_width / 15

        points_height = max_points_text_len / (points_width / points_font_size / 1.8)

        context = {"quest_form": quest_form, "points": points, "quest": quest, "formset": formset,
                   "points_table": points_table, "points_width": str(points_width),
                   "points_height": str(points_height),
                   "points_font_size": str(points_font_size)}

    return render(request, "graf_quests/get_quest.html", context=context)


def create_quest(request, character_id):
    if not request.user.is_authenticated:
        return redirect("login")

    character = Character.objects.get(id=character_id)
    quest = Quest(game=character.game, title="Название", description="Описание")
    quest.save()
    quest_point = QuestPoint(quest=quest, character=character, step=0, description="Шаг квеста")
    quest_point.save()
    return redirect("quest", quest_id=quest.id)


def delete_quest(request, quest_id, character_id):
    if not request.user.is_authenticated:
        return redirect("login")

    quest = Quest.objects.get(id=quest_id)
    game_id = quest.game.id
    quest.delete()
    if character_id > 0:
        return redirect("character", character_id)
    else:
        return redirect(get_all_quests, game_id=game_id)


def delete_quest_point(request, quest_point_id):
    if not request.user.is_authenticated:
        return redirect("login")

    quest_point = QuestPoint.objects.get(id=quest_point_id)
    quest_id = quest_point.quest.id
    quest_point.delete()
    return redirect("quest", quest_id)


def get_all_quests(request, game_id):
    if not request.user.is_authenticated:
        return redirect("login")

    quests = Quest.objects.filter(game__id=game_id)
    contex = {"quests": quests}
    return render(request, "graf_quests/all_quests.html", context=contex)


def get_all_characters_div(request):
    if not request.user.is_authenticated:
        return redirect("login")

    characters = Character.objects.all()
    resp_data = {}
    for c in characters:
        resp_data[c.id] = {"x": c.x, "y": c.y}

    return HttpResponse(json.dumps(resp_data), content_type="application/json")


def all_links(request, game_id):
    if not request.user.is_authenticated:
        return redirect("login")

    links = Link.objects.filter(game__id=game_id).order_by("character_1__id")
    contex = {"links": links}
    return render(request, "graf_quests/all_links.html", context=contex)


def edit_link(request):
    if not request.user.is_authenticated:
        return redirect("login")
    link_id = request.POST["link_id"]
    text = request.POST["text"]

    l = Link.objects.get(id=link_id)
    l.text = text

    if text == "" or text is None:
        l.delete()
    else:
        l.save()
    return HttpResponse("success")


def set_coord_by_id(request):
    if not request.user.is_authenticated:
        return redirect("login")
    character_id = request.POST["character_id"]

    c = Character.objects.filter(pk=character_id).first()
    c.x = int(float(request.POST["x"]))
    c.y = int(float(request.POST["y"]))

    c.save()

    return HttpResponse("success")


def create_character_link(request):
    if not request.user.is_authenticated:
        return redirect("login")

    first_character_id = int(request.POST["first_character_id"])
    second_character_id = int(request.POST["second_character_id"])
    text = request.POST["text"]

    first_character_id, second_character_id = (min(first_character_id, second_character_id),
                                               max(first_character_id, second_character_id))

    links = Link.objects.filter(character_1__id=first_character_id,
                                character_2__id=second_character_id)
    if len(links) > 0:
        links[0].delete()
    elif text == "" or text is None:
        pass
    else:
        character_1 = Character.objects.get(id=first_character_id)
        character_2 = Character.objects.get(id=second_character_id)
        link = Link(character_1=character_1,
                    character_2=character_2,
                    text=text,
                    game=character_1.game)
        link.save()

    return HttpResponse("success")
