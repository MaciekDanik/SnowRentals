from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Nazwa użytkownika',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Podaj hasło',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

INPUT_CLASSES = 'w-1/2 py-4 px-6 rounded-xl'

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',  'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Nazwa użytkownika',
        'class': INPUT_CLASSES
    }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Imię pracownika',
        'class': INPUT_CLASSES
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Nazwisko pracownika',
        'class': INPUT_CLASSES
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Podaj hasło',
        'class': INPUT_CLASSES
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Powtórz hasło',
        'class': INPUT_CLASSES
    }))