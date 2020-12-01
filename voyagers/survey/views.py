from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from .models import *
# from .forms import *
# from django.forms.models import inlineformset_factory
# from django.core.exceptions import PermissionDenied
from tourpackages.models import Attraction
import json
from django.http import HttpResponse
# Create your views here.


@login_required()
def survey(request):
    select_locations = Attraction.objects.values_list('city', 'country', 'attractionName', 'departure')
    di = {}
    vdi = []
    usa_city_list = ['New York', 'San Diego']
    usa_attraction_list = ['New York 3-day Adventure. Explore the City!', 'San Diego. Explore the most popular attractions in the city!']
    usa_departure = ['2021-05-06', '2021-05-10']

    china_city_list = ['Beijing', 'Shanghai']
    china_attraction_list = ['Discover Beijing!', 'Exploring Shanghai']
    china_departure = ['2021-04-07']

    france_city_list = ['Paris', 'Bordeax']
    france_attraction_list = ['Walk through the Streets of Paris!', 'Exploring Bordeaux']
    france_departure = ['2021-03-31']

    dubai_city_list = ['Dubai']
    dubai_attraction_list = ['Relish in the luxurious sands of Dubai!']
    dubai_departure = ['2021-03-20']

    england_city_list = ['London']
    england_attraction_list = ['Discover London!']
    england_departure = ['2021-04-04']

    sing_city_list = ['Singapore']
    sing_attraction_list = ['Amazing 3-day Adventure at Singapore!']
    sing_departure = ['2021-03-05']

    usa = [usa_city_list, usa_attraction_list, usa_departure]
   
    china = [china_city_list, china_attraction_list, china_departure]
    france = [france_city_list, france_attraction_list, france_departure]
    dubai = [dubai_city_list, dubai_attraction_list, dubai_departure]
    england = [england_city_list, england_attraction_list, england_departure]
    sing = [sing_city_list, sing_attraction_list, sing_departure]
    
    for a, b, c, d in select_locations:
        di.setdefault(b, []).append(a)
        di.setdefault(b, []).append(c)
        di.setdefault(b, []).append(d)

    di_keys = di.keys()
    

    di_value2 = di.get('China')
    di_value3 = di.get('Singapore')
    di_value3 = di.get('France')
    di_value4 = di.get('England')
    di_value5 = di.get('United Arab Emirates')

    # select_locations = [str(sl) for sl in select_locations]
    # select_locatreplaceions = [sl.replace("(","").replace(")","").("'","").replace(",","") for sl in select_locations]

    return render(request, 'survey.html', {'di_keys': di_keys, 'usa':usa,'china':china,'france':france, 'england':england,'sing':sing,'dubai':dubai})


def index(request):
    countries = Attraction.objects.get(all)
    print(countries)
    return render(request, 'surveytest.html', {'countries': countries})


def getdetails(request):
    # country_name = request.POST['country_name']
    country_name = request.GET['cnt']
    print("ajax country_name ", country_name)

    result_set = []
    all_cities = []
    answer = str(country_name[1:-1])
    selected_country = Attraction.objects.get(country=answer)
    print("selected country name ", selected_country)
    all_cities = selected_country.city.all()
    for city in all_cities:
        print("city name", attraction.city)
        result_set.append({'name': attraction.city})
    return HttpResponse(simplejson.dumps(result_set), mimetype='application/json',     content_type='application/json')

# def vote(request，question_id):
#     pk = request.user.pk
#     question = User.objects.get(pk=pk)
