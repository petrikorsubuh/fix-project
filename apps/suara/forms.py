from django import forms
from apps.tps import models as tp
from apps.partai import models as pt
from apps.caleg import models as cl
from apps.kecamatan import models as kc
from apps.kelurahan import models as kl


class SuaraForm(forms.Form):
    id = forms.CharField(required=False, widget=forms.HiddenInput)
    partai = forms.ModelChoiceField(queryset=pt.Partai.objects.all(),label='Pilih Partai', widget=forms.Select(attrs={
        'class': 'form-control'
    }))
    caleg = forms.ModelChoiceField(cl.Caleg.objects.all(),label='Pilih Caleg', widget=forms.Select(attrs={
        'class': 'form-control'
    }))
    kecamatan = forms.ModelChoiceField(kc.Kecamatan.objects.all(),label="Pilih Kecamatan")
    kelurahan = forms.ModelChoiceField(kl.Kelurahan.objects.all(),label="Pilih Kelurahan")
    tps = forms.ModelChoiceField(tp.Tps.objects.all(),label="Pilih TPS")
    jumlah_suara = forms.CharField(label='Jumlah', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }), required=False)

    pict = forms.ImageField(
        label='photo', widget=forms.FileInput(attrs={
            'class': 'form-control custome-file-input'
        }), required=False)
