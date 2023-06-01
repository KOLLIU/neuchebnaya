from django.contrib import admin

from graf_quests.models import Character, Link, Quest, QuestPoint, Game, ReadyGame, ReadyClub


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("title", "ready")


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ("game", "name", "role")
    fields = ("name", "role", "description", ("x", "y"), "game")
    list_filter = ("game",)


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ("character_1", "character_2", "text")
    list_display_links = ("text",)


@admin.register(Quest)
class QuestAdmin(admin.ModelAdmin):
    pass


@admin.register(QuestPoint)
class QuestPointAdmin(admin.ModelAdmin):
    list_display = ("quest", "character", "step")
    ordering = ("quest", "step")


@admin.register(ReadyGame)
class ReadyGameAdmin(admin.ModelAdmin):
    ordering = ("percent",)


@admin.register(ReadyClub)
class ReadyClubAdmin(admin.ModelAdmin):
    ordering = ("percent",)
