from django.shortcuts import render, redirect

from django.views import View

from apps.kecamatan.models import Kecamatan
from apps.kelurahan.models import Kelurahan
from apps.kelurahan.forms import KelurahanForm
from braces.views import LoginRequiredMixin, SuperuserRequiredMixin

from rest_framework import response,views,status
from apps.kelurahan import serializers


class KelurahanViews(LoginRequiredMixin, SuperuserRequiredMixin, View):
    login_url = '/login'
    template_name = 'kelurahan.html'

    def get(self, request):
        form = KelurahanForm(request.POST)
        kelurahans = Kelurahan.objects.all()

        return render(request, self.template_name, {
            'form': form,
            'kelurahan': kelurahans,
        })


class SaveKelurahanView(LoginRequiredMixin, SuperuserRequiredMixin, View):
    login_url = '/login'

    def post(self, request):
        form = KelurahanForm(request.POST)
        if form.is_valid():
            kelurahan = Kelurahan()
            # kc_id = form.cleaned_data['kecamatan']
            # kecamatan = Kecamatan.objects.get(pk=kc_id)

            # kelurahan.kecamatan = kecamatan
            kelurahan.kecamatan = form.cleaned_data['kecamatan']
            kelurahan.nama = form.cleaned_data['nama']
            kelurahan.save()

        return redirect('/kelurahan')


class EditKelurahanView(LoginRequiredMixin, SuperuserRequiredMixin, View):
    login_url = '/login'
    template_name = 'edit_kelurahan.html'

    def get(self, request, id):
        obj = Kelurahan.objects.get(id=id)
        data = {
            'id': obj.id,
            'kecamatan': obj.kecamatan,
            'nama': obj.nama
        }

        form = KelurahanForm(initial=data)
        kelurahan = Kelurahan.objects.all()

        return render(request, self .template_name, {
            'form': form,
            'kelurahan': kelurahan
        })


class UpdateKelurahanView(LoginRequiredMixin, SuperuserRequiredMixin, View):
    login_url = '/login'

    def post(self, request):
        form = KelurahanForm(request.POST)
        if form.is_valid():
            kelurahan = Kelurahan.objects.get(id=form.cleaned_data['id'])

            kelurahan.kecamatan=form.cleaned_data['kecamatan']
            kelurahan.nama = form.cleaned_data['nama']
            kelurahan.save()

        return redirect('/kelurahan')


class DeleteKelurahanView(LoginRequiredMixin, SuperuserRequiredMixin, View):
    login_url = '/login'

    def get(self, request, id):
        obj = Kelurahan.objects.get(id=id)
        obj.delete()

        return redirect('/kelurahan')


class TambahKelurahanView(LoginRequiredMixin, SuperuserRequiredMixin, View):
    login_url = '/login'
    template_name = 'tambah_kelurahan.html'

    def get(self, request):
        form = KelurahanForm(request.POST)
        kelurahans = Kelurahan.objects.all()
        kecamatans = Kecamatan.objects.all()        

        return render(request, self.template_name, {
            'form': form,
            'kelurahans': kelurahans,
            'kecamatans': kecamatans,
        })

class KelurahanService(views.APIView):

    def get(self, request):
        kecamatan = request.GET.get("kecamatan")
        kelurahans = Kelurahan.objects.filter(kecamatan_id=kecamatan).all()
        serializer=serializers.KelurahanSerializer(kelurahans,many=True)
        content = {
            "data":serializer.data,
        }
        return response.Response(content,status=status.HTTP_200_OK)