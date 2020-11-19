from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('editing/', views.editing, name='account'),
    url(r'^dashboard/$', views.dashboard, name='dashboard')
  
]

