from django import forms
from .models import DataCris


class DataCrisForm(forms.ModelForm):

    class Meta:
        model = DataCris
        fields = ["typ", "masa", "czystosc", "barwa", "pochodzenie", "wlasciciel"]

    typ = forms.CharField()
    masa = forms.CharField()
    czystosc = forms.CharField()
    barwa = forms.CharField()
    pochodzenie = forms.CharField()
    wlasciciel = forms.CharField()


class AddDataCrisForm(forms.ModelForm):

    class Meta:
        model = DataCris
        fields = ["typ", "masa", "czystosc", "barwa", "pochodzenie", "wlasciciel"]

    typ = forms.CharField()
    masa = forms.CharField()
    czystosc = forms.CharField()
    barwa = forms.CharField()
    pochodzenie = forms.CharField()
    wlasciciel = forms.CharField()

