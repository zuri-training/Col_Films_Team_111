from django.db import models

# Create your models here.
class Students(models.Model):
    first_name = models.CharField(max_length=100,)
    last_name = models.CharField(max_length=100,)
    email = models.CharField(max_length=250,)
    institution_name = models.CharField(max_length=200,)
    registration_number = models.CharField(max_length=100,)


    def __str__(self):
        return self.first_name + '--' + self.last_name + '--' + self.email
