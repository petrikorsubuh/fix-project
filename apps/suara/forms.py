from django import forms
from apps.dapil import models as dp
from apps.caleg import models as ca
from apps.tps import models as tp
class SuaraForm(forms.Form):
    id = forms.CharField(required = False,widget = forms.HiddenInput)   
    # dapil = forms.ModelChoiceField(queryset=dp.Dapil.objects.all(),label='Dapil',widget=forms.Select(attrs={
    #     'class':'form-control',
    #     # 'disabled': True
    # }),required=False)
    tps = forms.ModelChoiceField(queryset=tp.Tps.objects.all(),label='TPS',widget=forms.Select(attrs={'class': 'form-control'}),required=False)
    caleg = forms.ModelChoiceField(queryset=ca.Caleg.objects.all(),label='Caleg',widget=forms.Select(attrs={'class': 'form-control'}),required=False)
    jumlah_suara = forms.CharField(label='Jumlah',widget=forms.TextInput(attrs={
        'class':'form-control'
    }),required=False)

    pict= forms.ImageField(
    label='photo', widget=forms.FileInput(attrs={
        'class': ' custom-file-input'
    }),required=False)