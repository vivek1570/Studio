from django.urls import path

from . import views

app_name='todolist'

urlpatterns=[
    path('add/',views.add_todo,name='add_todo'),
    ]