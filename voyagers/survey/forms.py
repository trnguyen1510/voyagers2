from django import forms
from django.contrib.auth.models import User
from .models import Survey as Surveymodel
from django.forms import ModelForm

# countryChoices = [
#     ('US', 'United Stated of America'),
#     ('UAE', 'United Arab Emirates'),
#     ('Thai', 'Thailand'),
#     ('Sing', 'Singapore'),
#     ('France', 'France'),
#     ('England', 'England'),
#     ('China', 'China'),
#     ('Thailand', 'Thailand')
# ]
# cityChoices = [
#     ('Singapore', 'Singapore'),
#     ('San Diego', 'San Diego'),
#     ('New York', 'New York'),
#     ('Beijing', 'Beijing'),
#     ('Shanghai', 'Shanghai'),
#     ('Paris', 'Paris'),
#     ('Dubai', 'Dubai'),
#     ('Bordeaux', 'Bordeaux'),
#     ('London', 'London'),
#     ('Bangkok', 'Bangkok')

# ]
# tourChoices = [
#     ("New York 3-day Adventure. Explore the City!",
#      "New York 3-day Adventure. Explore the City!"),
#     ("San Diego. Explore the most popular attractions in the city!",
#      "San Diego. Explore the most popular attractions in the city!"),
#     ("Discover Beijing!", "Discover Beijing!"),
#     ("Exploring Shanghai", "Exploring Shanghai"),
#     ("Walk through the Streets of Paris!",
#      "Walk through the Streets of Paris!"),
#     ("Exploring Bordeaux", "Exploring Bordeaux"),
#     ("Discover London!", "Discover London!"),
#     ("Amazing 3-day Adventure at Singapore!",
#      "Amazing 3-day Adventure at Singapore!"),
#     ("Experience local cultural and heritage",
#      "Experience local cultural and heritage")

# ]

# departureChoices = [
#     ("2021-05-10", "2021-05-10"),
#     ("2021-01-16", "2021-01-16"),
#     ("2021-04-05", "2021-04-05"),
#     ("2021-07-20", "2021-07-20"),
#     ("2021-03-05", "2021-03-05"),
#     ("2021-04-07", "2021-04-07"),
#     ("2021-04-08", "2021-04-08"),
#     ("2021-03-31", "2021-03-31"),
#     ("2021-04-04", "2021-04-04")

# ]


class surveyForm(forms.ModelForm):
    class Meta:
        model = Surveymodel
        fields = ['country', 'city', 'tour',
                  'departure', 'futureCompanionDescription']

