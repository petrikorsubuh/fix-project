from django import forms
from apps.account import models

class AccountForm(forms.Form):
    id = forms.CharField(required = False,widget = forms.HiddenInput)
    name = forms.CharField(label='Nama User',widget=forms.TextInput(attrs={
        'class':'form-control'
    }),required=False)
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class': 'form-control'}),required=False)
    username = forms.CharField(label='User Name',widget=forms.TextInput(attrs={
        'class':'form-control'
    }),required=False)
    password = forms.CharField(label='Password User',widget=forms.PasswordInput(attrs={
        'class':'form-control'
    }),required=False)
    no_telpon = forms.CharField(label='No Telepone',widget=forms.TextInput(attrs={
        'class':'form-control'
    }),required=False)
    nik = forms.CharField(label='NIK',widget=forms.TextInput(attrs={
        'class':'form-control'
    }),required=False)

    gambar = forms.ImageField(
    label='gambar', widget=forms.FileInput(attrs={
        'class': ' custom-file-input'
    }),required=False)


    superuser = forms.CharField(required=False)