from django.shortcuts import render, redirect
from django.views import View
from apps.suara import forms
from apps.suara import models
from apps.kecamatan.models import Kecamatan
from apps.kelurahan.models import Kelurahan
from apps.partai.models import Partai
from apps.caleg.models import Caleg
from apps.tps.models import Tps
from apps.suara.models import Suara

from braces.views import LoginRequiredMixin
from django.http import HttpResponse


# Create your views here.
class TambahSuaraView(LoginRequiredMixin, View):

    login_url = '/login'
    template_name = 'suara_user.html'

    def get(self, request):
        
        partais = Partai.objects.filter(name='DEMOKRAT')
        partai = partais[0] if len(partais) > 0 else None
        caleg = []
        if partai:
            caleg = Caleg.objects.filter(partai=partai).all()
        
        form = forms.SuaraForm(request.POST)
        print(form)
        
        
        kecamatans = Kecamatan.objects.all()
        kelurahan = Kelurahan.objects.all()
        tpss = Tps.objects.all()
        suara = Suara.objects.all()

        return render(request, self.template_name, {
            "form": form,
            "partais": partais,
            "partai": partai,
            "caleg": caleg,
            "kecamatans": kecamatans,
            "kelurahan": kelurahan,
            "tpss": tpss,
            "suara": suara,
        })
        return redirect('')


class SaveSuaraView(LoginRequiredMixin, View):
    login_url = '/login'

    def post(self, request):
        form = forms.SuaraForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            # pt_id = form.cleaned_data['partai']
            # partai = Partai.objects.get(id=pt_id)
            # print(pt_id)

            # kc_id = form.cleaned_data['kecamatan']
            # kecamatan = Kecamatan.objects.get(id=kc_id)

            # tp_id = form.cleaned_data['tps']
            # tps = Tps.objects.get(id=tp_id)

            # ca_id = form.cleaned_data['caleg']
            # caleg = Caleg.objects.get(id=ca_id)

            # suara = models.Suara()
            # suara.partai = partai
            # suara.caleg = caleg
            # suara.kecamatan = kecamatan
            # suara.kelurahan = kelurahan
            # suara.tps = tps
            # suara.jumlah_suara = form.cleaned_data['jumlah_suara']
            # suara.pict = request.FILES['pict']
            # suara.save()

            suara = models.Suara()
            suara.partai = form.cleaned_data['partai']
            suara.caleg = form.cleaned_data['caleg']
            suara.kecamatan = form.cleaned_data['kecamatan']
            suara.kelurahan = form.cleaned_data['kelurahan']
            print(suara.kelurahan)
            suara.tps = form.cleaned_data['tps']
            suara.jumlah_suara = form.cleaned_data['jumlah_suara']
            suara.pict = request.FILES['pict']
            suara.save()

            return redirect('/relawan')

        return HttpResponse(form.errors)
