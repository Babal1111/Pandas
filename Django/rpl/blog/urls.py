from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),  
    path('edit/<int:blog_id>/', views.edit_blog, name='edit_blog'),
]

