from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Survey(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=100, blank=True, default='')
    city = models.CharField(blank=True,max_length=100, default='')
    tour = models.CharField(blank=True,max_length=100, default='')
    departure = models.CharField(blank=True, max_length=100, default='')
    futureCompanionDescription = models.TextField(blank=True, default='')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_surveyAnswer(sender, instance, created, **kwargs):
    if created:
        Survey.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_surveyAnswer(sender, instance, **kwargs):
    instance.survey.save()


# class Answer_Option(models.Model):
#     survey = models.ForeignKey(Question, on_delete=models.CASCADE)
#     text = models.CharField(max_length=200)
#
#     def __unicode__(self):
#         return self.text
