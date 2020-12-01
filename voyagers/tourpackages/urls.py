from django.urls import path
from . import views

urlpatterns = [
    path('tours/', views.tours, name='tours'),
    path('tourdetail/<int:pk>', views.detail, name='tourdetail')
    

]
