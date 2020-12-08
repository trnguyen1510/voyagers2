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







