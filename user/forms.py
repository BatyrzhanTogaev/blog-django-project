from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'password1', 'password2')