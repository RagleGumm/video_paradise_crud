from django.urls import path
from django.contrib.auth import views as auth_views
from movies import views

urlpatterns = [
    path("", views.movie_list, name="movie_list"),
    path("view/<int:pk>", views.movie_details, name="movie_view"),
    path("add", views.movie_add, name="movie_add"),
    path("edit/<int:pk>", views.movie_edit, name="movie_edit"),
    path("delete/<int:pk>", views.movie_delete, name="movie_delete"),
    path("search", views.find_movie, name="movie_search"),
    path("filter", views.filter_movies, name="movie_filter"),
    path("login", auth_views.LoginView.as_view(), name="login"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
]
