from django.shortcuts import render,redirect
from django.views import View
from apps.suara import forms
from apps.suara import models
from apps.kecamatan.models import  Kecamatan
from apps.kelurahan.models import Kelurahan
from apps.partai.models import Partai
from apps.caleg.models import Caleg
from apps.tps.models import Tps
from apps.suara.models import Suara
from .forms import SuaraForm

from django.views.generic import FormView

from braces.views import LoginRequiredMixin, SuperuserRequiredMixin

from django.http import HttpResponse
# Create your views here.
class TambahSuaraView(LoginRequiredMixin, SuperuserRequiredMixin,View):
    login_url = '/login'
    template_name = 'tambah_suara.html'

    def get(self, request):
        form = forms.SuaraForm(request.POST)
        partai =Partai.objects.all()
        caleg = Caleg.objects.all()
        kecamatan = Kecamatan.objects.all()
        kelurahan = Kelurahan.objects.all()
        tps = Tps.objects.all()
        suara = Suara.objects.all()

        return render(request, self.template_name,{
            "form":form,
            "partai":partai,
            "caleg":caleg,
            "kecamatan":kecamatan,
            "kelurahan":kelurahan,
            "tps":tps,
            "suara":suara,

        })


class SuaraView(LoginRequiredMixin, SuperuserRequiredMixin,View):
    login_url = '/login'
    template_name = 'suara.html'

    def get(self, request):
        form = forms.SuaraForm(request.POST)
        suara = models.Suara.objects.all()

        return render(request, self.template_name,{
            "form":form,
            "suaras":suara,
        })


class SaveSuaraView(LoginRequiredMixin, View):
    login_url = '/login'

    def post(self, request):
        form = forms.SuaraForm(request.POST, request.FILES)
        if form.is_valid():
            # pt_id = form.cleaned_data['partai']
            # partai = Partai.objects.get(id=pt_id) 

            # kc_id =form.cleaned_data['kecamatan']
            # kecamatan = Kecamatan.objects.get(id=kc_id)

            # tp_id = form.cleaned_data['tps']
            # tps = Tps.objects.get(id = tp_id)

            # ca_id = form.cleaned_data['caleg']
            # caleg = Caleg.objects.get(id = ca_id)

            suara = models.Suara()
            suara.partai = form.cleaned_data['partai']
            suara.caleg = form.cleaned_data['caleg']
            suara.kecamatan = form.cleaned_data['kecamatan']
            suara.kelurahan = form.cleaned_data['kelurahan']
            print(suara.kelurahan)
            suara.tps = form.cleaned_data['tps']
            suara.jumlah_suara = form.cleaned_data['jumlah_suara']
            if request.FILES.getlist('pict'):
                account.pict = request.FILES.getlist('pict')
            suara.save()

            return redirect ('/suara')
        return HttpResponse(form.errors)

class EditSuaraView(LoginRequiredMixin, SuperuserRequiredMixin, View):
    login_url = '/login'
    template_name = 'edit_suara.html'

    def get(self, request, id):
        obj = Suara.objects.get(id=id)
        data = {
            'id': obj.id,
            'partai':obj.caleg.partai,
            'caleg':obj.caleg,
            'kecamatan': obj.kecamatan,
            'kelurahan': obj.kelurahan,
            'tps': obj.tps,
            'jumlah_suara': obj.jumlah_suara,
            'pict': obj.pict
        }

        form = forms.SuaraForm(initial=data)
        suara = Suara.objects.all()

        return render(request, self.template_name, {
            'form': form,
            'suara': suara
        })


class UpdateSuaraView(LoginRequiredMixin, SuperuserRequiredMixin, View):
    login_url = '/login'

    def post(self, request):
        form = forms.SuaraForm(request.POST)
        if form.is_valid():
            suara = Suara.objects.get(id=form.cleaned_data['id'])
            suara.partai = form.cleaned_data['partai']
            suara.caleg = form.cleaned_data['caleg']
            suara.kecamatan = form.cleaned_data['kecamatan']
            suara.kelurahan = form.cleaned_data['kelurahan']
            suara.tps = form.cleaned_data['tps']
            suara.jumlah_suara = form.cleaned_data['jumlah_suara']
            suara.pict = request.FILES['pict']
            suara.save(force_update=True)

        return redirect('/suara')


class DeleteSuaraView(LoginRequiredMixin, SuperuserRequiredMixin, View):
    login_url = '/login'

    def get(self, request, id):
        obj = Suara.objects.get(id=id)
        obj.delete()

        return redirect('/suara')

#relawan


        