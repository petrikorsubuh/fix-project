from django import forms
from apps.tps import models as tp
class SuaraForm(forms.Form):
    id = forms.CharField(required = False,widget = forms.HiddenInput)   
    jumlah_suara = forms.CharField(label='Jumlah',widget=forms.TextInput(attrs={
        'class':'form-control'
    }),required=False)

    pict= forms.ImageField(
    label='photo', widget=forms.FileInput(attrs={
        'class': ' custom-file-input'
    }),required=False)