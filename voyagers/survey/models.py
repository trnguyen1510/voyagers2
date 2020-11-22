from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Question (models.Model):
    question = models.CharField(max_length=100)
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)
    option_four = models.CharField(max_length=30)

    def __unicode__(self):
        return self.question

# class Answer_Option(models.Model):
#     survey = models.ForeignKey(Question, on_delete=models.CASCADE)
#     text = models.CharField(max_length=200)
#
#     def __unicode__(self):
#         return self.text


class Answer_Count(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    answer_option = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.text



