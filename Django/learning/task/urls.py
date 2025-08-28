from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.task_list, name='task_list'),  # List all tasks
    path('todo/add/', views.task_add, name='task_add'),  # Add new task
    path('todo/update/<int:task_id>/', views.task_update, name='task_update'),  # Update task
    path('todo/delete/<int:task_id>/', views.task_delete, name='task_delete'),  # Delete task
]
    