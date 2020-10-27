from django.urls import path
from . import views

urlpatterns = [
    path('tours/', views.tours, name='tours'),

]