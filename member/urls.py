from django.urls import path
from django.conf.urls import url
from . import views

app_name='member'
urlpatterns = [
    path('logout/', views.logout,name='logout'),
    ]