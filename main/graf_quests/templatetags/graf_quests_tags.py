from django import template

from graf_quests.models import Game

register = template.Library()


@register.simple_tag(name="get_games_tag")
def get_games_tag():
    return Game.objects.filter(is_nav=True)
