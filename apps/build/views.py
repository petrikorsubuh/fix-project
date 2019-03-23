from django.shortcuts import render, redirect
from django.views import View

from apps.build import forms
from apps.build import models

# Create your views here.


class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        form = forms.LanguageForm(request.POST)
        languages = models.Language.objects.all()

        return render(request, self.template_name, {
            'form': form,
            'languages': languages
        })


class SaveLanguageView(View):
    def post(self, request):
        form = forms.LanguageForm(request.POST)
        if form.is_valid():
            language = models.Language()
            language.name = form.cleaned_data['name']
            language.creator = form.cleaned_data['creator']
            language.save()

        return redirect('/index')


class EditLanguageView(View):
    template_name = 'edit.html'

    def get(self, request, id):
        obj = models.Language.objects.get(id=id)
        data = {
            'id': obj.id,
            'name': obj.name,
            'creator': obj.creator
        }

        form = forms.LanguageForm(initial=data)
        languages = models.Language.objects.all()

        return render(request, self.template_name, {
            'form': form,
            'languages': languages
        })


class UpdateLanguageView(View):
    def post(self, request):
        form = forms.LanguageForm(request.POST)
        if form.is_valid():
            language =models.Language.objects.get(id=form.cleaned_data['id'])
            language.name = form.cleaned_data['name']
            language.creator = form.cleaned_data['creator']
            language.save()

        return redirect('/index')


class DeleteLanguageView(View):
       def get(self, request, id):
        obj = models.Language.objects.get(id=id)
        obj.delete()

        return redirect('/index')






# Kategory

class KategoriView(View):
    template_name ='kategori.html'
    def get(self, request):
        form = forms.KategoriCalegForm(request.POST)
        kategori =models.KategoriCaleg.objects.all()

        return render(request, self.template_name, {
            'form': form,
            'kategori': kategori
        })
    


class SaveKategoriView(View):
    template_name='kategori.html'
    def post(self, request):
        kat = forms.KategoriCalegForm(request.POST)
        if kat.is_valid():
            kategori=models.KategoriCaleg()
            kategori.name=kat.cleaned_data['name']
            kategori.save()
        return redirect('/kategori')

class EditKategoriView(View):
    template_name = 'edit_kategori.html'

    def get(self, request, id):
        obj=models.KategoriCaleg.objects.get(id=id)
        data ={
            'id':obj.id,
            'name':obj.name,
        }

        form = forms.KategoriCalegForm(initial=data)
        kategori = models.KategoriCaleg.objects.all()

        return render(request, self.template_name,{
            'form':form,
            'kategori': kategori
        })

class UpdateKategoriVIew(View):
    def post(self, request):
        kat = forms.KategoriCalegForm(request.POST)
        if kat.is_valid():
            kategori =models.KategoriCaleg.objects.get(id=kat.cleaned_data['id'])
            kategori.name=kat.cleaned_data['name']
            kategori.save()
        return redirect('/kategori')

class DeleteKategoriView(View):
    def get(self, request, id):
        obj = models.KategoriCaleg.objects.get(id=id)
        obj.delete()

        return redirect('/kategori')


#Tps
class TpsViews(View):
    template_name = 'tps.html'
    def get(self, request):
        form = forms.TpsForm(request.POST)
        tps = models.Tps.objects.all()

        return render(request,self.template_name,{
            'form':form,
            'tps':tps
        })


class TpsSaveViews(View):
    template_name = 'tps.html'

    def post(self, request):
        tp = forms.TpsForm(request.POST)

        if tp.is_valid():
            t=models.Tps()
            t.name = tp.cleaned_data['name']
            t.address=tp.cleaned_data['address']
            t.save()
        return redirect('/tps')


class EditTpsViews(View):
    template_name = 'edit_tps.html'
    def get(self ,request ,id):
        obj = models.Tps.objects.get(id=id)
        data={
            'id':obj.id,
            'name':obj.name,
            'address':obj.address,
        }
        form = forms.TpsForm(initial=data)
        tps = models.Tps.objects.all()

        return render (request ,self.template_name,{
            'form':form,
            'tps': tps
        })


class UpdateTpsViews(View):
    def post (self, request):
        tp = forms.TpsForm(request.POST)
        if tp.is_valid():
            t = models.Tps.objects.get(id=tp.cleaned_data['id'])
            t.name = tp.cleaned_data['name']
            t.address =tp.cleaned_data['address']
            t.save()
        return redirect ('/tps')


class DeleteTpsViews(View):
    def get (self ,id):
        obj = models.Tps.objects.get(id=id)
        obj.delete()
        return redirect('/tps')


# caleg
class CalegViews(View):
    template_name = 'caleg.html'
    def get(self, request):
        form = forms.CalegForm(request.POST)
        caleg = models.Caleg.objects.all()

        return render(request,self.template_name,{
            'form':form,
            'caleg':caleg
        })


class CalegSaveViews(View):
    template_name = 'caleg.html'

    def post(self, request):
        form = forms.CalegForm(request.POST)

        if caleg.is_valid():
            cal=models.Caleg()
            cal.name = caleg.cleaned_data['name']
            cal.nomor_urut=caleg.cleaned_data['no_urut']
            cal.kategoricaleg = caleg.cleaned_data
            cal.save()
        return redirect('/caleg')


class EditCalegViews(View):
    template_name='edit_caleg.html'

    def get (self, request, id):
        obj = models.Caleg.objects.get(id=id)
        data ={
            'id':obj.id,
            'kategori':obj.kategori,
            'partai':obj.partai,
            'dapil':obj.dapil,
            'name':obj.nama,
            'no_urut':obj.no_urut,
        }

        form = forms.DapilForm(initial=data)
        caleg = models.Caleg.objects.all()

        return render(request, template_name, {
            'form':form,
            'caleg':caleg,
        })


class UpdateCalegViews(View):
    def post(self, request):
        cal = forms.CalegForm(request.POst)
        if cal.is_valid():
            caleg = models.Caleg()
            caleg.name = cal.cleaned_data['name']
            caleg.nomor_urut = cal.cleaned_data['no_urut']
            caleg.kategoricaleg=cal.cleaned_data['kategoricaleg']
            caleg.partai=cal.cleaned_data['partai']
            caleg.dapil=cal.cleaned_data['dapil']
            caleg.save()
        return redirect('/caleg')


class DeleteCalegViews(View):
    def get(self, request, id):
        obj =models.Caleg.objects.get(id=id)
        obj.delete()

        return redirect ('/caleg')
            




