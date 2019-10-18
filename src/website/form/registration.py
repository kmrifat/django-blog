from _ast import keyword

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.core.exceptions import ValidationError

from ..models import Profile
from ..models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
