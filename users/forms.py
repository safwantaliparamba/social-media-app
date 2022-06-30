from django import forms

from django.contrib.auth.models import User

from users.models import Author


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'strong password'}),
            'email': forms.EmailInput(attrs={'class':  'form-control'}),
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'password'})
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = ('user',)
