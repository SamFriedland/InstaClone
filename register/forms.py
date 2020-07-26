from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

YEARS = [x for x in range(1900,2030)]

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    d_o_b = forms.DateTimeField(label='Date of birth',
                                widget=forms.SelectDateWidget(years=YEARS))

    class Meta:
        model = User
        fields = ["username","email","password1","password2", "d_o_b",]