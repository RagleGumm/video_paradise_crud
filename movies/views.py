from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import MovieSearchForm, MovieForm, MovieFilter
from .models import Movie


# Create your views here.
@login_required
def get_movie(
    request,
    template_name="movies/movie_search.html"
):
    if request.method == "POST":
        form = MovieSearchForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data["search_condition"]
            movie = Movie.objects.filter(main_title__icontains=cd)
            data = {}
            data["object_list"] = movie
            return render(request, "movies/movie_list.html", data)
    else:
        form = MovieSearchForm()
    return render(request, template_name, {"form": form})


@login_required
def filter_movie(
    request,
    template_name="movies/movie_filter.html"
):
    if request.method == "POST":
        form = MovieFilter(request.POST)
        if form.is_valid():
            sel_genre = form.cleaned_data["genre"]
            sel_medium = form.cleaned_data["medium"]
            sel_rating = form.cleaned_data["rating"]
            movie = Movie.objects.filter(
                genre=sel_genre, medium=sel_medium, rating=sel_rating
            )
            data = {}
            data["object_list"] = movie
            return render(request, "movies/movie_list.html", data)
    else:
        form = MovieFilter()
    return render(request, template_name, {"form": form})


@login_required
def movie_list(
    request,
    template_name="movies/movie_list.html"
):
    movie = Movie.objects.all()
    data = {}
    data["object_list"] = movie
    return render(request, template_name, data)


@login_required
def movie_view(
    request,
    pk,
    template_name="movies/movie_detail.html"
):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, template_name, {"object": movie})


@login_required
def movie_create(
    request,
    template_name="movies/movie_form.html"
):
    form = MovieForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("movie_list")
    return render(request, template_name, {"form": form})


@login_required
def movie_update(
    request,
    pk,
    template_name="movies/movie_form.html"
):
    movie = get_object_or_404(Movie, pk=pk)
    form = MovieForm(request.POST or None, instance=movie)
    if form.is_valid():
        form.save()
        return redirect("movie_list")
    return render(request, template_name, {"form": form})


@login_required
def movie_delete(
    request,
    pk,
    template_name="movies/movie_confirm_delete.html"
):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        movie.delete()
        return redirect("movie_list")
    return render(request, template_name, {"object": movie})
