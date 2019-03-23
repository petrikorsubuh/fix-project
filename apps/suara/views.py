from django.shortcuts import render,redirect
from django.views import View
from apps.suara import forms
from apps.suara import models
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
            suara = models.Suara()
            # suara.dapil = form.cleaned_data['dapil']
            suara.tps = form.cleaned_data['tps']
            suara.caleg = form.cleaned_data['caleg']
            suara.jumlah_suara = form.cleaned_data['jumlah_suara']
            suara.save()

        return redirect ('/suara')