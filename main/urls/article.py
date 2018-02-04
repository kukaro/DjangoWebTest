from django.contrib import admin
from django.urls import path
from main import views

app_name = 'article'
urlpatterns = [
    path('<str:bid>/write/', views.Write.as_view(), name='write')
]
