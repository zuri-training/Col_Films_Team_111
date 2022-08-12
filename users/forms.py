import email
from django import forms

class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailField)
    password = forms.CharField(widget=forms.PasswordInput)