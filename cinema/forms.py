from django import forms
from django.conf import settings

from cinema.models import Movie
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.forms import ValidationError



class CreateMoviesForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = 'title descriptions director'.split()

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите название!',
                    'rows': 10
                }
            ),
            'descriptions': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Описание'
                }
            ),
            'director': forms.Select(
                attrs={
                    'class': 'form-control form-control-custom',

                }
            )
        }

class LoginForms(forms.Form):
    username = forms.CharField(label='user name',widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter username',
            'rows': 10
        }
    ))
    password = forms.CharField(label='password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter password'
        }
    ))




class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='user name', help_text='100 characters', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-email', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

