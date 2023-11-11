
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('tasks/',views.todo_list_create_view,name='list_create_todo'),
    path('tasks/<int:pk>',views.todo_retrieve_view,name='retrieve_todo'),
    path('tasks/<int:pk>',views.todo_delete_view,name='delete_todo'),
]
