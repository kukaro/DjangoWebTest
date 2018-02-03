from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


class UserRegisterForm(forms.Form):
    id = forms.CharField(label='id', max_length=30)
    nick = forms.CharField(label='nick', max_length=30)
    stud_no = forms.IntegerField(label='student number')
    email = forms.EmailField(label='email')
    pw_hash = forms.CharField(label='password', max_length=128)
    pw_hash_verify = forms.CharField(label='password verify', max_length=128)
    pnt = forms.IntegerField(label='point')
