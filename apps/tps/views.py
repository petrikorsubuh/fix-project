from django.shortcuts import render,redirect
from django.views import View
# Create your views here.
from apps.tps import models
from apps.tps import forms

from apps.kelurahan.models import Kelurahan

from braces.views import LoginRequiredMixin,SuperuserRequiredMixin

class IndexTpsView(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url ='/login'
    template_name = 'tps.html'
    def get(self, request):
        form = forms.TpsForm(request.POST)
        tps = models.Tps.objects.all()


        return render(request, self.template_name,{
            'form':form,
            'tps':tps,
        })


class SaveTpsView(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url ='/login'
    def post(self, request):
        form = forms.TpsForm(request.POST)
        if form.is_valid():
            kl_id = form.cleaned_data['kl_id']
            kelurahan = Kelurahan.objects.get(id = kl_id)

            tps = models.Tps()
            tps.kelurahan =kelurahan
            tps.alamat = form.cleaned_data['address']
            tps.name = form.cleaned_data['name']
            tps.save()
            return redirect('/tps')


class EditTpsView(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url ='/login'
    template_name = 'edit_tps.html'
    def get(self, request, id):
        obj=models.Tps.objects.get(id=id)
        data ={
            'id':obj.id,
            'id':obj.kelurahan,
            'alamat':obj.alamat,
            'name':obj.name,
        }

        form = forms.TpsForm(initial=data)
        tps = models.Tps.objects.all()

        return render(request, self.template_name,{
            'form':form,
            'tps':tps
            })

    # def post(self, request, id):
    #     form = forms.TpsForm(request.POST)
    #     # print(form.is_valid())
    #     if form.is_valid():
    #         tps =models.Tps.objects.get(id=id)
    #         tps.name=form.cleaned_data['name']
    #         tps.address = form.cleaned_data['address']
    #         tps.save()
    #     return redirect('/tps')


class UpdateTpsView(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url ='/login'
    def post(self, request):
        form = forms.TpsForm(request.POST)

        if form.is_valid():
            kl_id = form.cleaned_data['kl_id']
            kelurahan = Kelurahan.objects.get(id = kl_id)

            tps = models.Tps.objects.get(id=form.cleaned_data['id'])
            tps.kelurahan = kelurahan
            tps.alamat = form.cleaned_data['alamat']
            tps.name = form.cleaned_data['name']
            tps.save()
            return redirect ('/tps')

    


class DeleteTpsViews(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url ='/login'
    def get(self, request, id):
        obj = models.Tps.objects.get(id=id)
        obj.delete()

        return redirect('/tps')

class TambahTpsView(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url ='/login'
    template_name = 'tambah_tps.html'

    def get(self, request):
        form = forms.TpsForm(request.POST)
        tps =models.Tps.objects.all()

        return render (request,self.template_name,{
            'form':form,
            'tps':tps
        })
    def post(self, request):
        form = forms.TpsForm(request.POST)
        if form.is_valid():
            kl_id = form.cleaned_data['kl_id']
            kelurahan = Kelurahan.objects.get(id = kl_id)

            tps=models.Tps()
            tps.kelurahan = kelurahan
            tps.alamat = form.cleaned_data['alamat']
            tps.name = form.cleaned_data['name']
            tps.save()
            return redirect('/tps')
