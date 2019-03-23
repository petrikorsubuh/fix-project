from django import forms

class PartaiForm(forms.Form):
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    name =forms.CharField(
        label='Nama partai', widget=forms.TextInput(attrs={
            'class': 'form-control',
            'required' : True
        }))
    no_urut= forms.IntegerField(
        label='Nomor Urut', widget=forms.NumberInput(attrs={
            'class':'form-control'
        }))
    gambar = forms.ImageField(
        label='Gambar Partai', widget=forms.FileInput(attrs={
            'class': ' custom-file-input'
        }))
