from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserform(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'photo',]


class CustomUserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label="Имя пользователя",
        widget=forms.TextInput(attrs={'class': 'your-input-class'}),
        help_text='',
    )
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={'class': 'your-input-class'}),
        help_text='',
    )
    password2 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={'class': 'your-input-class'}),
        help_text='',
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']
