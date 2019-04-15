from django.shortcuts import render, redirect
from django.views import View
# Create your views here.
from apps.tps import models
from apps.tps import forms

from apps.kelurahan.models import Kelurahan

from braces.views import LoginRequiredMixin, SuperuserRequiredMixin

from rest_framework import views, response, status
from apps.tps import serializers
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

class IndexTpsView(LoginRequiredMixin, SuperuserRequiredMixin, View):
    login_url = '/login'
    template_nama = 'tps.html'

    def get(self, request):
        form = forms.TpsForm(request.POST)
        tps = models.Tps.objects.all()

        return render(request, self.template_nama, {
            'form': form,
            'tps': tps,
        })


class SaveTpsView(LoginRequiredMixin, SuperuserRequiredMixin, View):
    login_url = '/login'

    def post(self, request):
        form = forms.TpsForm(request.POST)
        if form.is_valid():
            # kl_id = form.cleaned_data['kelurahan']
            # kelurahan = Kelurahan.objects.get(id=kl_id)

            tps = models.Tps()
            # tps.kelurahan = kelurahan
            tps.kelurahan= form.cleaned_data['kelurahan']
            tps.alamat = form.cleaned_data['alamat']
            tps.nama = form.cleaned_data['nama']
            tps.save()
            return redirect('/tps')


class EditTpsView(LoginRequiredMixin, SuperuserRequiredMixin, View):
    login_url = '/login'
    template_nama = 'edit_tps.html'

    def get(self, request, id):
        obj = models.Tps.objects.get(id=id)
        data = {
            'id': obj.id,
            'kelurahan': obj.kelurahan,
            'alamat': obj.alamat,
            'nama': obj.nama,
        }

        form = forms.TpsForm(initial=data)
        tps = models.Tps.objects.all()

        return render(request, self.template_nama, {
            'form': form,
            'tps': tps
        })


class UpdateTpsView(LoginRequiredMixin, SuperuserRequiredMixin, View):
    login_url = '/login'

    def post(self, request):
        form = forms.TpsForm(request.POST)

        if form.is_valid():
            tps = models.Tps.objects.get(id=form.cleaned_data['id'])
            tps.kelurahan = form.cleaned_data['kelurahan']
            tps.alamat = form.cleaned_data['alamat']
            tps.nama = form.cleaned_data['nama']
            tps.save()
            return redirect('/tps')


class DeleteTpsViews(LoginRequiredMixin, SuperuserRequiredMixin, View):
    login_url = '/login'

    def get(self, request, id):
        obj = models.Tps.objects.get(id=id)
        obj.delete()

        return redirect('/tps')


class TambahTpsView(LoginRequiredMixin, SuperuserRequiredMixin, View):
    login_url = '/login'
    template_nama = 'tambah_tps.html'

    def get(self, request):
        form = forms.TpsForm(request.POST)
        tps = models.Tps.objects.all()
        kelurahans = Kelurahan.objects.all()

        return render(request, self.template_nama, {
            'form': form,
            'tps': tps,
            'kelurahans': kelurahans,
        })

    def post(self, request):
        form = forms.TpsForm(request.POST)
        if form.is_valid():
            # kl_id = form.cleaned_data['kelurahan']
            # kelurahan = Kelurahan.objects.get(id=kl_id)

            tps = models.Tps()
            # tps.kelurahan = kelurahan
            tps.kelurahan = form.cleaned_data['kelurahan']
            tps.alamat = form.cleaned_data['alamat']
            tps.nama = form.cleaned_data['nama']
            tps.save()
            return redirect('/tps')


class TpsService(LoginRequiredMixin, views.APIView):

    # parser_classes=(JSONParser)

    def get(self, request):
        kelurahan = request.GET.get('kelurahan')
        tpss = models.Tps.objects.filter(kelurahan=kelurahan).all()
        serializer = serializers.TpsSerializer(tpss, many=True)
        content = {
            "data": serializer.data,
        }
        return response.Response(content, status=status.HTTP_200_OK)

    @csrf_exempt
    def post(self, request):
        tpss = serializers.TpsSerializer(data=request.data)
        if tpss.is_valid():
            tpss.save()

            content = {
                "data": tpss.data,
            }
            return response.Response(content, status=status.HTTP_201_CREATED)
        return response.Response({
            'message':'Request is not valid'
        },status=status.HTTP_400_BAD_REQUEST)