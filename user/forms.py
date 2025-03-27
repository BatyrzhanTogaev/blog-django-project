from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.forms.widgets import ClearableFileInput



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


class CustomClearableFileInput(ClearableFileInput):
    template_name = 'widgets/custom_clearable_file_input.html'



class CustomUserEditForm(forms.ModelForm):
    username = forms.CharField(
        label='Никнэйм',
        widget=forms.TextInput(attrs={'class': 'edit-text'}),
        help_text= '',
    )
    photo = forms.ImageField(
        label='Фотография',
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'edit-photo'}),
    )
    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={'class': 'edit-text'}),
        help_text='',
    )
    last_name = forms.CharField(
        label='фамилия',
        widget=forms.TextInput(attrs={'class': 'edit-text'}),
        help_text='',
    )
    email = forms.CharField(
        label='Почта',
        widget=forms.TextInput(attrs={'class': 'edit-text'}),
        help_text='',
    )
    
    class Meta:
        model = CustomUser
        fields = ['username', 'photo', 'first_name', 'last_name', 'email',]