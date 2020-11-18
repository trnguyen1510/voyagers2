# test open and load of default page
import pytest
import validators
from django.contrib.auth.models import User
from django.urls import reverse
from home.models import User_Profile
from tourpackages.models import Attraction


def pageloader():
    page = "http://127.0.0.1:8000/home/"
    return page


def test_load():
    assert validators.url(pageloader())

#Database helpers testing
@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    assert User.objects.count() == 1

#User_profile(home) testing
@pytest.mark.django_db
def test_user_Profile_create():
    contact = User_Profile.objects.create(first_name='John', last_name='Doe', Address='111', Country='USA')
    assert contact.first_name == 'John'

@pytest.mark.django_db
def test_attraction_create():
    tour = Attraction.objects.create(city='la', attractionName='boat', attractionDescription='boatisfun', price='11')
    assert tour.city == 'la'

#Client testing
@pytest.mark.django_db
def test_view_home(client):
   url = reverse('index')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_view_dashboard(client):
   url = reverse('dashboard')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_view_tours(client):
   url = reverse('tours')
   response = client.get(url)
   assert response.status_code == 200





