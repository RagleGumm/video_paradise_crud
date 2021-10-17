from django.db import models
from django.urls import reverse

# Create your models here.


class Movie(models.Model):
    GENRE_CHOICES = (
        ("horror", "horror"),
        ("sci-fi", "sci-fi"),
        ("thriller", "thriller"),
        ("action", "action"),
        ("comedy", "comedy"),
        ("drama", "drama"),
    )
    MEDIUM_CHOICES = (
        ("dvd", "dvd"),
        ("dvd-r", "dvd-r"),
        ("cd", "cd"),
        ("cd-r", "cd-r"),
        ("vcd", "vcd"),
        ("vhs", "vhs"),
    )
    RATING_CHOICES = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    )

    main_title = models.CharField(max_length=200)
    other_titles = models.CharField(
        max_length=200,
        blank=True
    )
    production_year = models.CharField(
        max_length=9,
        blank=True
    )
    production_country = models.CharField(
        max_length=3,
        default="",
        blank=True
    )
    genre = models.CharField(
        choices=GENRE_CHOICES,
        max_length=200,
        blank=True
    )
    medium = models.CharField(
        choices=MEDIUM_CHOICES,
        max_length=200,
        blank=True
    )
    rating = models.CharField(
        choices=RATING_CHOICES,
        max_length=1,
        blank=True
    )
    comments = models.CharField(
        max_length=200,
        blank=True
    )
    image = models.ImageField(
        upload_to='uploads/%Y/%m/%d',
        blank=True
    )

    class Meta:
        ordering = ("main_title",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("movie_edit", kwargs={"pk": self.pk})
