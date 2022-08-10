from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie
from moviepy.editor import *


def list_film(request):
    
    film = Movie.objects.all()
    data = {
        'film': film,
    }
    return render(request, 'list_film.html', data)

def add_favourite(request, id):
    film = get_object_or_404(Movie, id=id)
    user = request.user
    if film.favourites.filter(id=request.user.id).exists():
        film.favourites.remove(request.user)
    else:
        film.favourites.add(request.user)
        return redirect('favourites')
    return redirect('favourites')

def list_favourites(request):
    favs = Movie.objects.filter(favourites=request.user)
    return render(request, 'favourites.html', {'favs':favs})