from django.shortcuts import render
from django.views import generic
from .forms import CustomUserCreationForm


# Create your views here.
class Register(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'main/register.html'
