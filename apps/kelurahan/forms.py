from django import forms
# from apps.kelurahan import forms 
from apps.kecamatan import models

class KelurahanForm(forms.Form):
    id = forms.CharField(required = False, widget=forms.HiddenInput())
    kecamatan=forms.ModelChoiceField(queryset=models.Kecamatan.objects.all(), label="Kecamatan", widget=forms.Select(attrs={
        "class": "form-control",
    }))
    nama = forms.CharField(label='kelurahan', widget=forms.TextInput(attrs={
            'class': 'form-control',}))
