from django.shortcuts import render, redirect

from django.views import View

from apps.partai import models
from apps.partai import forms

from braces.views import LoginRequiredMixin, SuperuserRequiredMixin

class IndexPartaiView(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url ='/login'
    template_name = 'partai.html'

    def get(self, request):
        form = forms.PartaiForm(request.POST)
        partai = models.Partai.objects.all()

        return render(request, self.template_name, {
            'form': form,
            'partai': partai
        })


class SavePartaiView(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url ='/login'
    def post(self, request):
        form = forms.PartaiForm(request.POST, request.FILES)
        if form.is_valid():
            partai = models.Partai()
            partai.name = form.cleaned_data['name']
            partai.no_urut = form.cleaned_data['no_urut']
            partai.gambar = request.FILES['gambar']
            partai.save()
        return redirect('/partai')


class EditPartaiView(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url ='/login'
    template_name = 'edit_partai.html'

    def get(self, request, id):
        obj = models.Partai.objects.get(id=id)
        data = {
            'id': obj.id,
            'name': obj.name,
            'no_urut' : obj.no_urut,
            'gambar':obj.gambar
        }

        form = forms.PartaiForm(initial=data)
        partai = models.Partai.objects.all()

        return render(request, self.template_name, {
            'form': form,
            'partai': partai
        })


class UpdatePartaiView(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url ='/login'
    def post(self, request):
        form = forms.PartaiForm(request.POST,request.FILES)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            partai = models.Partai.objects.get(id=form.cleaned_data['id'])
            partai.name = form.cleaned_data['name']
            partai.no_urut = form.cleaned_data['no_urut']
            partai.gambar = request.FILES['gambar']
            partai.save()

        return redirect('/partai')


class DeletePartaiView(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url ='/login'
    def get(self, request, id):
        obj = models.Partai.objects.get(id=id)
        obj.delete()

        return redirect('/partai')


class TambahPartaiView(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url ='/login'
    template_name = 'tambah_partai.html'

    def get(self, request):
        form = forms.PartaiForm(request.POST)
        partai = models.Partai.objects.all()

        return render(request,self.template_name,{
            'form':form,
            'partai':partai,
        })
    
