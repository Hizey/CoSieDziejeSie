from django.forms import ModelForm
from tinymce.widgets import TinyMCE
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Room


class RoomForm(ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={"cols": 80, "rows": 30}))

    class Meta:
        model = Room
        fields = "__all__"


class Register_User_Form(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']