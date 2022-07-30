from calendar import c
import email
from telnetlib import STATUS
from django.db import models
from django.utils.translation import gettext_lazy as _


from django.contrib.auth import get_user_model
from django.conf import settings

from users.models import NewUser


CATEGORY_CHOICES = (
    ('A' , 'ACTION'),
    ('D', 'DRAMA'),
    ('R', 'ROMANCE')
)
STATUS_CHOICES = (
    ('in_review','in review'),
    ('approved','approved')

)
class Movie(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    category =  models.CharField(choices=CATEGORY_CHOICES, max_length=1)
    uploader = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    status = models.CharField(choices=CATEGORY_CHOICES, max_length=1)
    movie_length = models.IntegerField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

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
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    value = models.IntegerField()

    def __str__(self):
        return str(self.user)
    class Meta:
        unique_together = ("user", "movie", "value")
# Create your models here.
