from django import forms
from apps.build import models


class LanguageForm(forms.Form):
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    name = forms.CharField()
    creator = forms.CharField()









