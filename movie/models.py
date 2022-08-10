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


STATUS_CHOICES = (
    ('in_review','in review'),
    ('approved','approved')

)
class Movie(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    category =  models.CharField(choices=CATEGORY_CHOICES, max_length=1)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(choices=CATEGORY_CHOICES, max_length=1)
    movie_length = models.CharField(max_length=100)
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

class Param(models.Model):
    movies_length_max = models.IntegerField()
    review_upload = models.BooleanField()
    #movies_size_max = 

class Prefence(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    value = models.IntegerField()

    def __str__(self):
        return str(self.user)
    class Meta:
        unique_together = ("user", "movie", "value")
# Create your models here.
