from django import template
from ..models import Movie

register = template.Library()


@register.simple_tag
def total_movies():
    """Tag returning count of movies in the database."""
    return Movie.objects.count()
