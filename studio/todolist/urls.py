from django.urls import path

from . import views

app_name='todolist'

urlpatterns=[
    path('add/',views.add_todo,name='add_todo'),
    path('<uuid:pk>/',views.detail,name='detail'),
    path('<uuid:pk>/edit/',views.edit,name='edit'),
    ]