from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Attraction(models.Model):
    city = models.CharField(max_length=50, default='')
    country = models.CharField(max_length=50, default='')
    attractionName = models.CharField(max_length=150, default='')
    day1 = models.TextField(default='')
    day1_Description = models.TextField(default='')
    day1_condition = models.TextField(default='')
    day2 = models.TextField(default='')
    day2_Description = models.TextField(default='')
    day2_condition = models.TextField(default='')
    day3 = models.TextField(default='')
    day3_Description = models.TextField(default='')
    day3_condition = models.TextField(default='')
    guideDescription = models.TextField(default='')
    departure = models.DateField(null=True, blank=True)
    price = models.FloatField()
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.attractionName

    @property
    def imageURL(self):
        try:
            url = self.image1.url
        except:
            url = ''
        return url

   
    def imageURL2(self):
        try:
            url = self.image2.url
        except:
            url = ''
        return url

    
    def imageURL3(self):
        try:
            url = self.image3.url
        except:
            url = ''
        return url
