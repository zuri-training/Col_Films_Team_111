from calendar import c
import email
from telnetlib import STATUS
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.conf import settings

from users.models import NewUser

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', args=(str(self.id)))

CATEGORY_CHOICES = Category.objects.all().values_list('name', 'name')

choice_list = []
for item in CATEGORY_CHOICES:
    choice_list.append(item)


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp4', '.3gp']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class Movie(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    thumbnail = models.ImageField(upload_to='movies/thumbnails/%y%m%d', null=True, blank=True)
    movie = models.FileField(upload_to='movies/movie/%y%m%d', validators=[validate_file_extension], null=True)
    category =  models.TextField(choices=CATEGORY_CHOICES)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    length = models.CharField(max_length=100, null=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True, null=True)
    favourites = models.ManyToManyField(User, related_name='favourite', default=None, blank=True)
    likes = models.ManyToManyField(User, related_name='movie_likes')
    dislikes = models.ManyToManyField(User, related_name='movie_dislikes')


    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()

    def __str__(self):
        return self.title

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField()

    def __str__(self):
        return f'comment by {self.email} on {self.movie}'

