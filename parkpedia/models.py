from django.db import models
from django.contrib.auth.models import User


class Park(models.Model):
    name = models.CharField(max_length=128, unique=False)
    parkId = models.IntegerField(default=0)
    facilities = models.CharField(max_length=128, unique=False, default="None")
    streetNum = models.IntegerField(default=0)
    streetName = models.CharField(max_length=128, unique=False)
    washroom = models.CharField(max_length=10, unique=False)
    latLon = models.CharField(max_length=40, unique=False)
    imageURL = models.CharField(max_length=1000, unique=False, default="None")

    def __unicode__(self):  # For Python 2, use __str__ on Python 3
        return self.name


class FavouritePark(models.Model):
    user = models.ForeignKey(User, blank=True)
    username = models.CharField(max_length=500)
    name = models.CharField(max_length=128, unique=False)

    def __unicode__(self):
        return self.name

