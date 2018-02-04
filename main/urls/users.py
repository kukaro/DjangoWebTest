from django.contrib import admin
from django.urls import path
from main import views

app_name = 'users'
urlpatterns = [
    path('register/', views.Register.as_view(), name='register')
]
