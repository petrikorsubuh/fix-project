from django import forms


class TpsForm(forms.Form):
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    kelurahan = forms.CharField()
    alamat = forms.CharField(label="alamat", widget=forms.TextInput(attrs={
        "class": "form-control",
        "required": True
    }))
    name = forms.CharField(label="Nama TPS", widget=forms.TextInput(attrs={
        "class": "form-control",
        "required": True
    }))
