from django import forms


class TpsForm(forms.Form):
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    kecamatan = forms.CharField(label="kecamatan", widget=forms.TextInput(attrs={
        "class": "form-control",
        "required": True
    }))
    kelurahan = forms.CharField(label="kelurahan", widget=forms.TextInput(attrs={
        "class": "form-control",
        "required": True
    }))
    address = forms.CharField(label="address", widget=forms.TextInput(attrs={
        "class": "form-control",
        "required": True
    }))
    name = forms.CharField(label="Nama TPS", widget=forms.TextInput(attrs={
        "class": "form-control",
        "required": True
    }))
