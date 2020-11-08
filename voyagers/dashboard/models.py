from django.db import models

# Create your models here.
class Profile(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50, default='abcde')
    date_of_birth = models.DateField(auto_now=False)
    twitter_handle = models.CharField(max_length=20)
    fb_handle = models.CharField(max_length=20)
    insta_handle = models.CharField(max_length=20)
    telephone = models.CharField(max_length=13)
    address1 = models.TextField()
    address2 = models.TextField()
    city = models.CharField(max_length=30)
    state  = models.CharField(max_length=30)
    zipcode = models.IntegerField(blank=True, null=True)
    profile_pic = models.ImageField()
    about = models.TextField()

    def __str__(self):
        return 'Profile #{}'.format(self.id)

    class Meta:
        verbose_name_plural = 'profiles'