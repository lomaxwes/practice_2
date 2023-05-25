from django import forms
from django.contrib.auth.models import User


class BaseRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class CodeLoginForm(forms.Form):
    username = forms.CharField()
    code = forms.CharField()
