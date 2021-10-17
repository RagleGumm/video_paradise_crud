from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import MovieSearchForm, MovieForm, MovieFilter
from .models import Movie


@login_required
def find_movie(request):
    """Returns list of movies meeting search form criteria."""
    if request.method == "POST":
        form = MovieSearchForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data["search_condition"]
            movie = Movie.objects.filter(main_title__icontains=cd)
            return render(
                request=request,
                template_name="movies/movie_list.html",
                context={"object_list": movie}
            )
    else:
        form = MovieSearchForm()
        return render(
            request=request,
            template_name="movies/movie_search.html",
            context={"form": form}
        )


@login_required
def filter_movies(request):
    """Returns list of movies meeting filter form criteria."""
    if request.method == "POST":
        form = MovieFilter(request.POST)
        if form.is_valid():
            sel_genre = form.cleaned_data["genre"]
            sel_medium = form.cleaned_data["medium"]
            sel_rating = form.cleaned_data["rating"]
            movie = Movie.objects.filter(
                genre=sel_genre,
                medium=sel_medium, 
                rating=sel_rating
            )
            return render(
                request=request,
                template_name="movies/movie_list.html",
                context={"object_list": movie}
            )
    else:
        form = MovieFilter()
        return render(
            request=request,
            template_name="movies/movie_filter.html",
            context={"form": form}
        )


@login_required
def movie_list(request):
    """Displays full movie list."""
    movie = Movie.objects.all()
    return render(
        request=request,
        template_name="movies/movie_list.html",
        context={"object_list": movie}
    )


@login_required
def movie_details(request, pk):
    """Displays detailed view of selected movie."""
    movie = get_object_or_404(Movie, pk=pk)
    return render(
        request=request,
        template_name="movies/movie_detail.html",
        context={"object": movie}
    )


@login_required
def movie_add(request):
    """Allows adding new movie."""
    form = MovieForm(request.POST or None, files=request.FILES)
    if form.is_valid():
        form.save()
        return redirect("movie_list")
    else:
        return render(
            request=request,
            template_name="movies/movie_form.html",
            context={"form": form}
        )


@login_required
def movie_edit(request, pk):
    """Allows editing movie details."""
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':                                 
        form = MovieForm(data=request.POST, instance=movie, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("movie_list")
    else:
        form = MovieForm(request.POST or None, instance=movie)
        return render(
            request=request,
            template_name="movies/movie_form.html",
            context={"form": form}
        )


@login_required
def movie_delete(request, pk):
    """Allows deletion of selected movie."""
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        movie.delete()
        return redirect("movie_list")
    else:
        return render(
            request=request,
            template_name="movies/movie_confirm_delete.html",
            context={"object": movie}
        )
