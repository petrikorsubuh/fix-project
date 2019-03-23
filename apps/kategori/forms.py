from django import forms


class KategoriCalegForm(forms.Form):
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    name = forms.CharField(label="Nama Kategori", widget=forms.TextInput(attrs={
        "class": "form-control",
        "required": True
    }))