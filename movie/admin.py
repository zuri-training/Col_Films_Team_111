from django.contrib import admin
from .models import *
admin.site.register(Movie)

admin.site.register(Comment)
admin.site.register(Category)

# Register your models here.
