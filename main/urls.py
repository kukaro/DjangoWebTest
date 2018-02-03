from django.contrib import admin
from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('register/', views.Register.as_view(), name='register')
]
