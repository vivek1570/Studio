from django.urls import path 
from django.contrib.auth import views as auth_views

from . import views 

app_name='account'

urlpatterns=[
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.custom_logout,name='logout')
]