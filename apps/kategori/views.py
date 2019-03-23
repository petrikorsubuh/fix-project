from django.shortcuts import render,redirect

from django.views import View

from apps.kategori.models import KategoriCaleg
from apps.kategori.forms import KategoriCalegForm
from braces.views import LoginRequiredMixin,SuperuserRequiredMixin


class IndexKategoriViews(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url = '/login'
    template_name = 'kategori.html'

    def get(self, request):
        form = KategoriCalegForm(request.POST)
        kategori = KategoriCaleg.objects.all()

        return render(request, self.template_name, {
            'form':form,
            'kategori':kategori,
        })


class SaveKategoriView(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url = '/login'
    def post(self, request):
        form = KategoriCalegForm(request.POST)
        if form.is_valid():
            Kategori = KategoriCaleg()
            Kategori.name = form.cleaned_data['name']
            Kategori.save()

        return redirect('/kategori')


class EditKategoriView(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url = '/login'
    template_name = 'edit_kategori.html'

    def get(self, request, id):
        obj = KategoriCaleg.objects.get(id=id)
        data = {
            'id':obj.id,
            'name':obj.name
        }

        form = KategoriCalegForm(initial=data)
        kategori = KategoriCaleg.objects.all()

        return render(request,self.template_name,{
            'form':form,
            'kategori':kategori
        })


class UpdateKategoriView(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url = '/login'

    def post(self, request):
        form = KategoriCalegForm(request.POST)
        if form.is_valid():
            kategori = KategoriCaleg.objects.get(id=form.cleaned_data['id'])
            kategori.name = form.cleaned_data['name']
            kategori.save(force_update=True)

        return redirect('/kategori')


class DeleteKategoriView(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url = '/login'
    def get(self, request, id):
        obj = KategoriCaleg.objects.get(id=id)
        obj.delete()

        return redirect ('/kategori')


class TambahKategoriView(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url = '/login'
    template_name = 'tambah_kategori.html'

    def get(self, request):
        form = KategoriCalegForm(request.POST)
        kategori = KategoriCaleg.objects.all()

        return render(request, self.template_name, {
            'form':form,
            'kategori':kategori
        })