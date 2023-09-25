from django.db import models

# Create your models here.

class trailers(models.Model) :
    plate = models.CharField(max_length=8)
    location = models.CharField(max_length=8)
    company = models.CharField(max_length=15)

class yardInfo(models.Model):

    saveDate = models.DateField(auto_now_add=True)
    editDate = models.DateField(auto_now=True)
    status = models.CharField(max_length=5)
    partDesc = models.CharField(max_length=50)
    plate = models.CharField(max_length=8)


