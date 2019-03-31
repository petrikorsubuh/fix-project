from django import forms

class KecamatanForm(forms.Form):
    id = forms.CharField(required= False, widget=forms.HiddenInput())
    nama = forms.CharField(label= 'Nama Kecamatan', widget= forms.TextInput(attrs={
        "class":"form-control",
        "required": True
    }))
 