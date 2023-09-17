from django.db import models

# Create your models here.

class trailers(models.Model) :
    plate = models.CharField(max_length=8)
    location = models.CharField(max_length=8)
    company = models.CharField(max_length=15)

class trailerLocation(models.Model):
    date = models.DateField()
    class Meta:
        ordering = ('date',)
    