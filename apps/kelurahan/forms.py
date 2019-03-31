from django import forms


class KelurahanForm(forms.Form):
    id = forms.CharField(required = False, widget=forms.HiddenInput())
    kecamatan = forms.CharField()
    nama = forms.CharField()