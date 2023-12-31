from django.urls import path
from . import views

urlpatterns = [
    path('accounts/', views.get_all_accounts),
    path('submitted/', views.add_account),
    path('movies/movie-ratings/<int:movie_id>/', views.movie_rating),
    path('movies/movie-ratings/', views.movie_ratings),
]