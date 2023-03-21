from django.forms import ModelForm
from tinymce.widgets import TinyMCE
from django import forms

from .models import Room


class RoomForm(ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = Room
        fields = "__all__"
