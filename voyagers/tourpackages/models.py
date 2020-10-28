from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Attraction(models.Model):
    city = models.CharField(max_length=30, default='')
    attractionName = models.CharField(max_length=100)
    attractionDescription = models.TextField()
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.attractionName


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Location(models.Model):
    city = models.CharField(max_length=30)
    region = models.CharField(max_length=2)
    #image = models.CharField(max_length=200)

    def __str__(self):
        return self.city



class Package(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
