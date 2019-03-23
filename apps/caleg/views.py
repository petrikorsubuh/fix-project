from django.shortcuts import render,redirect
from django.views import View

from apps.caleg import models
from apps.caleg import forms
from braces.views import LoginRequiredMixin, SuperuserRequiredMixin

class CreateCalegView(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url = '/login'
    template_name = 'caleg.html'

    def get(self, request):
        form = forms.CalegForm(request.POST)
        caleg = models.Caleg.objects.all()

        return render(request,self.template_name,{
            'form': form,
            'caleg': caleg
        })


class SaveCalegView(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url = '/login'
    def post(self, request):
        form = forms.CalegForm(request.POST)
        if form.is_valid():
            caleg = models.Caleg()
            caleg.name = form.cleaned_data['name']
            caleg.nomor_urut = form.cleaned_data['no_urut']
            caleg.dapil = form.cleaned_data['dapil']
            caleg.partai = form.cleaned_data['partai']
            caleg.kategoricaleg = form.cleaned_data['kategori']
            caleg.save()

        return redirect('/caleg')


class EditCalegView(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url = '/login'
    template_name = 'edit_caleg.html'

    def get(self, request, id):
        obj = models.Caleg.objects.get(id=id)
        data ={
            'id':obj.id,
            'name':obj.name,
            'no_urut':obj.nomor_urut,
            'dapil':obj.dapil,
            'partai':obj.partai,
            'kategori':obj.kategoricaleg
        }

        form = forms.CalegForm(initial=data)
        caleg = models.Caleg.objects.all()

        return render(request,self.template_name,{
            'form':form,
            'caleg':caleg
        })


class UpdateCalegView(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url = '/login'
    def post(self, request):
        form = forms.CalegForm(request.POST)
        if form.is_valid():
            caleg = models.Caleg.objects.get(id=form.cleaned_data['id'])
            caleg.name = form.cleaned_data['name']
            caleg.nomor_urut = form.cleaned_data['no_urut']
            caleg.dapil = form.cleaned_data['dapil']
            caleg.partai = form.cleaned_data['partai']
            caleg.kategoricaleg = form.cleaned_data['kategori']
            caleg.save()
        return redirect('/caleg')


class DeleteCalegView(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url = '/login'
    def get(self, request, id):
        obj = models.Caleg.objects.get(id=id)
        obj.delete()

        return redirect('/caleg')

class TambahCalegView(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url = '/login'
    template_name = 'tambah_caleg.html'
    def get(self, request):
        form = forms.CalegForm(request.POST)
        caleg =models.Caleg.objects.all()

        return render(request,self.template_name,{
            "form":form,
            "caleg":caleg,
        })