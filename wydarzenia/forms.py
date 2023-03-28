from django.forms import ModelForm
from tinymce.widgets import TinyMCE
from django import forms

from .models import Room


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ('host', 'topic', 'name', 'price', 'description', 'date', 'time', 'location')
        labels = {
            'description': "Opisz wydarzenie",
            'host': "",
            'topic': "",
            'name': "",
            'price': "",
            'date': "",
            'time': "",
            'location': "",
        }
        widgets = {
            'host': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Host'}),
            'topic': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Kategoria'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nazwa wydarzenia'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cena'}),
            'date': forms.SelectDateWidget(attrs={'class': 'form-control', 'placeholder': 'Data'}),
            'time': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Godzina rozpoczęcia'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lokalizacja'}),
        }
        description = forms.CharField(widget=TinyMCE(attrs={"cols": 80, "rows": 30}))
