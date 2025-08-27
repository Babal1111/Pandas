from django.urls import path
from . import views

urlpatterns = [
    path('', views.odd_even_checker, name='odd_even_checker'),
]
