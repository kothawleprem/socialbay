from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings


urlpatterns = [
    path('',views.home, name='home'),
    #path('contact/', views.contact, name='contact'),
 
]
