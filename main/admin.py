from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('id', 'sid', 'username', 'pw_hash', 'password')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(NavigationGroup)
admin.site.register(Board)
admin.site.register(Article)
admin.site.register(NavigationItem)
