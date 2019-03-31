from django import forms
# from apps.dapil import models

class DapilForm(forms.Form):
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    name = forms.CharField(label="Nama dapil", widget=forms.TextInput(attrs={
        "class": "form-control",
        "required": True
    }))
    alamat = forms.CharField(label="Alamat dapil", widget=forms.Textarea(attrs={
        "class": "form-control",
        "rows": 3
    }))
