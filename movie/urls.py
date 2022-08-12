from django.urls import path
from .views import DeleteMovie, index, my_movies, modal, movie_detail, dashboard, create_movie, list_movie,add_favourite, list_favourites, add_likes, add_dislikes

urlpatterns = [
    path('', index, name="home"),
    path('add_movie/', create_movie, name="add_movie"),
    path('delete/<int:pk>/', DeleteMovie.as_view(), name="delete"),
    path('list_movie/', list_movie, name="list_movie"),
    path('detail/<int:pk>/', movie_detail, name="detail"),
    path('dashboard/<int:pk>', dashboard, name="dashboard"),
    path('add_favourites/<int:id>/', add_favourite, name="add_favourites"),
    path('favourites/', list_favourites, name="favourites"),
    path('like/<int:pk>/', add_likes, name="like"),
    path('dislike/<int:pk>/', add_dislikes, name="dislike"),
    path('modal/', modal, name="modal"),
    path('my_movies/', my_movies, name="my_movies"),
]