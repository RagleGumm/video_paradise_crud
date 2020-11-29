from django.urls import path
from django.contrib.auth import views as auth_views
from movies import views

urlpatterns = [
    path("", views.movie_list, name="movie_list"),
    path("view/<int:pk>", views.movie_view, name="movie_view"),
    path("new", views.movie_create, name="movie_new"),
    path("edit/<int:pk>", views.movie_update, name="movie_edit"),
    path("delete/<int:pk>", views.movie_delete, name="movie_delete"),
    path("search", views.get_movie, name="movie_search"),
    path("filter", views.filter_movie, name="movie_filter"),
    path("login", auth_views.LoginView.as_view(), name="login"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
]
