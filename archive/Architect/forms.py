from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

# class UserRegisterForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": 'new-password'})
    )
    password2 = forms.CharField(
        label='Password confirmation',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": 'new-password'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('name', 'password1', 'password2')