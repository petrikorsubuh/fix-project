from django.shortcuts import render, redirect
from django.views import View

from apps.dapil import forms
from apps.dapil import models
from braces.views import LoginRequiredMixin, SuperuserRequiredMixin, StaffuserRequiredMixin

# Create your views here.
# crude dapil


class DapilView(LoginRequiredMixin, SuperuserRequiredMixin, View):
    login_url = '/login'
    template_name = 'dapil.html'

    def get(self, request):
        form = forms.DapilForm(request.POST)
        dapil = models.Dapil.objects.all()

        return render(request, self.template_name, {
            'form': form,
            'dapil': dapil
        })


class SaveDapilView(LoginRequiredMixin, SuperuserRequiredMixin, View):
    login_url = '/login'
    def post(self, request):
        dap = forms.DapilForm(request.POST)
        if dap.is_valid():
            dapil = models.Dapil()
            dapil.name = dap.cleaned_data['name']
            dapil.address = dap.cleaned_data['address']
            dapil.save()
        return redirect('/dapil')


class EditDapilView(LoginRequiredMixin, SuperuserRequiredMixin, View):
    login_url = '/login'
    template_name = 'edit_dapil.html'

    def get(self, request, id):
        obj = models.Dapil.objects.get(id=id)
        data = {
            'id': obj.id,
            'name': obj.name,
            'address': obj.address,
        }

        form = forms.DapilForm(initial=data)
        dapil = models.Dapil.objects.all()

        return render(request, self.template_name, {
            'form': form,
            'dapil': dapil
        })


class UpdateDapilView(LoginRequiredMixin, SuperuserRequiredMixin, View):
    login_url = '/login'
    def post(self, request):
        dap = forms.DapilForm(request.POST)
        if dap.is_valid():
            dapil = models.Dapil.objects.get(id=dap.cleaned_data['id'])
            dapil.name = dap.cleaned_data['name']
            dapil.address = dap.cleaned_data['address']
            dapil.save()
        return redirect('/dapil')


class DeleteDapilView(LoginRequiredMixin, SuperuserRequiredMixin, View):
    login_url = '/login'
    def get(self, request, id):
        obj = models.Dapil.objects.get(id=id)
        obj.delete()

        return redirect('/dapil')


class TambahDapilView(LoginRequiredMixin, SuperuserRequiredMixin, View):
    login_url = '/login'
    template_name = 'tambah_dapil.html'

    def get(self, request):
        form = forms.DapilForm(request.POST)
        dapil = models.Dapil.objects.all()

        return render(request, self.template_name, {
            'form': form,
            'dapil': dapil
        })

    def post(self, request):
        dap = forms.DapilForm(request.POST)
        # print(dap.is_valid())
        if dap.is_valid():
            dapil = models.Dapil()
            dapil.name = dap.cleaned_data['name']
            dapil.address = dap.cleaned_data['address']
            dapil.save()
        return redirect('/dapil')
