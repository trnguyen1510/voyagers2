from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('about/',views.about, name='about'),
    path('login/', views.login, name='login'),
    path('signup/',views.signup, name='signup'),
    path("logout/", auth_views.LogoutView.as_view(template_name='index.html'), name='logout'),

]


