from django import forms
from django.forms import ModelForm
from .models import Movie


class MovieForm(ModelForm):
    """Form for displaying movie details."""
    class Meta:
        model = Movie
        fields = [
            "main_title",
            "other_titles",
            "production_year",
            "production_country",
            "genre",
            "medium",
            "rating",
            "comments",
            "image"
        ]


class MovieSearchForm(forms.Form):
    """Form allowing to find movie using title."""
    search_condition = forms.CharField(
        label="Search by title:",
        max_length=100
    )


class MovieFilter(ModelForm):
    """Form allowing filtering movies according to genre, medium & rating."""
    class Meta:
        model = Movie
        fields = ["genre", "medium", "rating"]
