from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.http import HttpResponse

from apps.account import forms
from apps.account import models
from braces.views import LoginRequiredMixin,SuperuserRequiredMixin


class IndexAccountView(LoginRequiredMixin, SuperuserRequiredMixin, View):
    template_name = 'account.html'

    def get(self, request):
        form = forms.AccountForm(request.POST)
        account = models.Account.objects.all()

        return render(request, self.template_name, {
            'form': form,
            'account': account
        })


class SaveAccountView(LoginRequiredMixin, SuperuserRequiredMixin, View):


    login_url='/login'
    def post(self, request):
        form = forms.AccountForm(request.POST)
        if form.is_valid():
            user = User()
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password'])
            user.email = form.cleaned_data['email']

            superuser = form.cleaned_data['superuser']
            
            if superuser == 'on':
                user.is_superuser = True
                user.is_staff = False
            else:
                user.is_superuser = False
                user.is_staff = True
            user.save()

            account = models.Account()
            account.user = user
            account.name = form.cleaned_data['name']
            account.no_telpon = form.cleaned_data['no_telpon']
            account.nik = form.cleaned_data['nik']
            account.gambar = request.FILES['gambar']
            account.save()
            return redirect('/account')

        return HttpResponse(form.errors)

class EditAccountView(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url='/login'
    template_name = 'edit_account.html'

    def get(self, request, id):
        obj = models.Account.objects.get(id=id)
        data = {
            'id': obj.id,
            'name': obj.user,
            'name': obj.name,
            # 'email':obj.email,
            # 'username':obj.username,
            # 'password':obj.password,
            'no_telpon': obj.no_telpon,
            'nik': obj.nik,
            'gambar':obj.gambar,
        }
        form = forms.AccountForm(initial=data)
        account = models.Account.objects.all()

        return render(request, self.template_name, {
            'form': form,
            'account': account,
        })


class UpdateAccountView(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url='/login'
    def post(self, request):
        form = forms.AccountForm(request.POST)
        if form.is_valid():
            account = models.Account.objects.get(id=form.cleaned_data['id'])
            account.name = form.cleaned_data['name']
            account.email = form.cleaned_data['email']
            # account.user = form.cleaned_data['user']
            account.username = form.cleaned_data['username']
            account.password = form.cleaned_data['password']
            account.no_telpon = form.cleaned_data['no_telpon']
            account.nik = form.cleaned_data['nik']
            print(form.cleaned_data['gambar'])
            account.gambar = request.FILES['gambar']
            account.save(force_update=True)

            return redirect('/account')
        
        return HttpResponse(form.errors)


class DeleteAccountView(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url='/login'
    def get(self, request, id):
        obj = models.User.objects.get(id=id)
        obj.delete()

        
        return redirect('/account')


class TambahAccountView(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url='/login'
    template_name = 'tambah_account.html'

    def get(self, request):
        form = forms.AccountForm(request.POST)
        account = models.Account.objects.all()

        return render(request, self.template_name, {
            'form': form,
            'account': account,
        })
