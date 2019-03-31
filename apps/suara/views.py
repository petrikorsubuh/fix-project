from django.shortcuts import render,redirect
from django.views import View
from apps.suara import forms
from apps.suara import models
from apps.kecamatan.models import  Kecamatan
from apps.partai.models import Partai
from apps.caleg.models import Caleg
# Create your views here.
class TambahSuaraView(View):
    template_name = 'tambah_suara.html'

    def get(self, request):
        form = forms.SuaraForm(request.POST)
        suara = models.Suara.objects.all()

        return render(request, self.template_name,{
            "form":form,
            "suara":suara,
        })


class SuaraView(View):
    template_name = 'suara.html'

    def get(self, request):
        form = forms.SuaraForm(request.POST)
        suara = models.Suara.objects.all()

        return render(request, self.template_name,{
            "form":form,
            "suara":suara,
        })


class SaveSuaraView(View):

    def post(self, request):
        form = forms.SuaraForm(request.POST)
        if form.is_valid():
            kc_id =form.cleaned_data['kecamatan']
            kecamatan = Kecamatan.objects.get(id=kc_id)

            pt_id = form.cleaned_data['partai']
            partai = Partai.objects.get(id = pt_id)

            ca_id = form.cleaned_data['calon']
            calon = Caleg.objects.get(id = ca_id)

            suara = models.Suara()
            suara.partai = partai
            suara.caleg = calon
            suara.kecamatan = kecamatan
            suara.jumlah_suara = form.cleaned_data['jumlah_suara']
            suara.save()

        return redirect ('/suara')