from django import forms
from apps.kategori import models as mk
from apps.partai import models as mp
from apps.dapil import models as md

class CalegForm(forms.Form):
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    kategori=forms.ModelChoiceField(queryset=mk.KategoriCaleg.objects.all(),label="Kategori", widget=forms.Select(attrs={
        "class": "form-control",
    }))
    partai=forms.ModelChoiceField(queryset=mp.Partai.objects.all(), label="Partai", widget=forms.Select(attrs={
        "class": "form-control",
    }))
    dapil=forms.ModelChoiceField(queryset=md.Dapil.objects.all(), label="Dapil", widget=forms.Select(attrs={
        "class": "form-control",
    }))
    name= forms.CharField(label="Name", widget=forms.TextInput(attrs={
        "class": "form-control",
    }))
    no_urut =forms.IntegerField(label="Nomor Urut", widget=forms.TextInput(attrs={
        "class": "form-control",
    }))