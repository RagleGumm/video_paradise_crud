from django import forms
from django.forms import ModelForm
from .models import Movie


class MovieForm(ModelForm):
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
    search_condition = forms.CharField(
        label="Search by title:",
        max_length=100
    )


class MovieFilter(ModelForm):
    class Meta:
        model = Movie
        fields = ["genre", "medium", "rating"]
