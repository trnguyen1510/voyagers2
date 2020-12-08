from django.urls import path
from . import views
from dashboard.views import dashboard

urlpatterns = [
    path('survey/', views.survey, name='survey'),

    # path('ajax/load-cities/', views.load_cities, name='ajax_load_cities')
]
