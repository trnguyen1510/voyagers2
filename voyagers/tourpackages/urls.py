from django.urls import path
from . import views

urlpatterns = [
    path('tours/', views.tours, name='tours'),
<<<<<<< HEAD
=======
    path('tourdetail/', views.detail, name='tourdetail')
>>>>>>> e41371ada3c229faca904d093d87e097858decb5

]