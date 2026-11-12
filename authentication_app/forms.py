from django import forms
from authentication_app.models import *
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username','email','user_type','bio','avatar','password1','password2',]