from django import template
from ..models import Movie

register = template.Library()


@register.simple_tag
def total_movies():
    return Movie.objects.count()
