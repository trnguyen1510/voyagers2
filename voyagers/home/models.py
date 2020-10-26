from django.db import models


# Create your models here.
class User_Profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    Address = models.TextField()
    Country = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name


# class customer(models.Model):
#     username=models.CharField(max_length=10)
#     email = mdoels.e