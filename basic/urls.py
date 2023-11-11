
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('tasks/',views.todo_list_create_view,name='list_create_todo'),
]
