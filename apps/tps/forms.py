from django import forms

from apps.kelurahan import models

class TpsForm(forms.Form):
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    kelurahan = forms.ModelChoiceField(queryset=models.Kelurahan.objects.all(), label='Kelurahan',widget=forms.Select(attrs={
        "class":'form-control',
    }))
    alamat = forms.CharField(label="alamat", widget=forms.TextInput(attrs={
        "class": "form-control",
        "required": True
    }))
    nama = forms.CharField(label="Nama TPS", widget=forms.TextInput(attrs={
        "class": "form-control",
        "required": True
    }))
