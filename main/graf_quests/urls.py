from django.urls import path

from .views import index, get_all_characters_div, set_coord_by_id, get_character, get_quest, delete_quest_point, \
    create_quest, get_all_quests, delete_quest, edit_link, all_links, create_character_link, create_character, \
    get_all_characters, return_print_text, calculator

urlpatterns = [
    # path("", index, name="graf_quests"),

    path("<int:game_id>", index, name="graf_quests"),

    # character
    path("character/<int:character_id>", get_character, name="character"),
    path("create_character/<int:game_id>", create_character, name="create_character"),
    path("all_characters/<int:game_id>", get_all_characters, name="all_characters"),
    path("return_print_text/<int:game_id>", return_print_text, name="return_print_text"),

    # quest
    path("quest/<int:quest_id>", get_quest, name="quest"),
    path("create_quest/<int:character_id>", create_quest, name="create_quest"),
    path("delete_quest_point/<int:quest_point_id>", delete_quest_point, name="delete_quest_point"),
    path("all_quests/<int:game_id>", get_all_quests, name="all_quests"),
    path("delete_quest/<int:quest_id>/<int:character_id>", delete_quest, name="delete_quest"),

    # links
    path("edit_link", edit_link, name="edit_link"),
    path("all_links/<int:game_id>", all_links, name="all_links"),
    path("create_character_link", create_character_link, name="create_character_link"),

    # graf
    path("get_all_characters_div", get_all_characters_div, name="get_all_characters_div"),
    path("set_coord_by_id", set_coord_by_id, name="set_coord_by_id"),

    # local_for_smena
    path("calculator", calculator, name="calculator"),
]
