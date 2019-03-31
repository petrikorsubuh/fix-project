from django.shortcuts import render,redirect

# Create your views here.
from django.views import View

from apps.kecamatan.models import Kecamatan
from apps.kecamatan.forms import KecamatanForm
from braces.views import LoginRequiredMixin,SuperuserRequiredMixin

class KecamatanView(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url = '/login'
    template_name = 'kecamatan.html'

    def get(self, request):
        form = KecamatanForm(request.POST)
        kecamatan = Kecamatan.objects.all()

        return render(request,self.template_name,{
            "form":form,
            "kecamatan":kecamatan,
        })


class SaveKecamatanView(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url = '/login'

    def post(self, request):
        form = KecamatanForm(request.POST)
        if form.is_valid():
            print(form)
            kecamatan = Kecamatan()
            kecamatan.nama = form.cleaned_data['nama']
            kecamatan.save()


        return redirect('/kecamatan')


class EditKecamatanView(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url = '/login'
    template_name = 'edit_kecamatan.html'

    def get(self, request, id):
        obj = Kecamatan.objects.get(id=id)
        data = {
            'id':obj.id,
            'nama':obj.nama,
        }

        form = KecamatanForm(initial=data)
        kategori = Kecamatan.objects.all()

        return render(request,self.template_name,{
            'form':form,
            'kecamatan':kecamatan
        })


class UpdateKecamatanView(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url = '/login'

    def post(self, request):
        form = KecamatanForm(request.POST)
        if form.is_valid():
            kecamatan = Kecamatan.objects.get(id=form.cleaned_data['id'])
            kecamatan.name = form.cleaned_data['name']
            kecamatan.save(force_update=True)

        return redirect('/kecamatan')


class DeleteKecamatanView(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url = '/login'
    def get(self, request, id):
        obj = Kecamatan.objects.get(id=id)
        obj.delete()

        return redirect ('/kecamatan')


class TambahKecamatanView(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url = '/login'
    template_name = 'tambah_kecamatan.html'

    def get(self, request):
        form = KecamatanForm(request.POST)
        kecamatan = Kecamatan.objects.all()

        return render(request, self.template_name, {
            'form':form,
            'kategori':kecamatan
        })