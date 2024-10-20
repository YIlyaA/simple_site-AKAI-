from django import forms
from .models import DataCris


class DataCrisForm(forms.ModelForm):
    class Meta:
        model = DataCris
        fields = ["typ", "masa", "czystosc", "barwa", "pochodzenie", "wlasciciel"]


class AddDataCrisForm(forms.ModelForm):
    class Meta:
        model = DataCris
        fields = ["typ", "masa", "czystosc", "barwa", "pochodzenie", "wlasciciel"]
