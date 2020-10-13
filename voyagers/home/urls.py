from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('about/',views.about, name='about'),
    path('login/', views.login, name='login'),
    path('signup/',views.signup, name='signup')


]


