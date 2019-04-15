from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.http import HttpResponse

# from apps.account import forms
# from apps.account import models
from braces.views import LoginRequiredMixin,SuperuserRequiredMixin


# from django.views.generic import CreateView,UpdateView,FormView,DeleteView
from apps.account.models import Account
from apps.account.forms import AccountForm


class IndexAccountView(LoginRequiredMixin, SuperuserRequiredMixin, View):
    login_url='/login'
    template_name = 'account.html'

    def get(self, request):
        form = AccountForm(request.POST)
        account =Account.objects.all()

        return render(request, self.template_name, {
            'form': form,
            'accounts': account
        })


# # class AccountCreateViews(CreateView,LoginRequiredMixin,SuperuserRequiredMixin):
# #     login_url='/login'
# #     template_name='tambah_account.html'
# #     form_class=AccountForm
# #     model= Account
# #     success_url='account.html'


# # class AccountUpdateViews(LoginRequiredMixin,SuperuserRequiredMixin,FormView):
# #     login_url='/login'
# #     template_name = 'edit_account.html'
# #     form_class = AccountForm


# #     def get_object(self, pk):
# #         return Account.objects.get(pk=pk)

# #     def get_queryset(self):
# #         return Account.objects.all()

# #     def get_form(self):
# #         obj = self.get_object(pk=self.kwargs['pk'])
# #         return AccountForm(self.request.POST, instance=obj)

# #     def get_context_data(self, **kwargs):
# #         ctx = super(AccountUpdateViews, self).get_context_data(**kwargs)
# #         ctx['object'] = self.get_object(pk=self.kwargs['pk'])
# #         ctx['accounts'] = self.get_queryset()
# #         return ctx

# #     def form_valid(self, form):
# #         form.save()

# #         print('valid')
# #         return redirect('/account')

# #     def form_invalid(self, form):
# #         print('invalid')
# #         return HttpResponse(form.errors)

# class DeleteAccountView(LoginRequiredMixin,SuperuserRequiredMixin,DeleteView):
#     model = Account
#     success_url = '/account'

#     def get(self, *args, **kwargs):
#         return self.post(*args, **kwargs)

class SaveAccountView(LoginRequiredMixin, SuperuserRequiredMixin, View):
    login_url='/login'
    def post(self, request):
        form=AccountForm(request.POST)
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

            account = Account()
            account.user = user
            account.name = form.cleaned_data['name']
            account.no_telpon = form.cleaned_data['no_telpon']
            account.nik = form.cleaned_data['nik']
            if request.FILES.getlist('gambar'):
                account.gambar = request.FILES.getlist('gambar')
            account.save()
            return redirect('/account')

        return HttpResponse(form.errors)





class EditAccountView(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url='/login'
    template_name = 'edit_account.html'

    def get(self, request, id):
        obj = Account.objects.get(id=id)
        data = {
            'id': obj.id,
            'user': obj.user,
            'name': obj.name,
            'email':obj.email,
            'username':obj.username,
            'password':obj.password,
            'no_telpon': obj.no_telpon,
            'nik': obj.nik,
            'gambar':obj.gambar,
        }
        form = AccountForm(initial=data)
        account = Account.objects.all()

        return render(request, self.template_name, {
            'form': form,
            'account': account,
        })


class UpdateAccountView(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url='/login'
    def post(self, request):
        form = AccountForm(request.POST)
        if form.is_valid():
            account = Account.objects.get(id=form.cleaned_data['id'])
            account.name = form.cleaned_data['name']
            account.email = form.cleaned_data['email']
            # account.user = form.cleaned_data['user']
            account.username = form.cleaned_data['username']
            account.password = form.cleaned_data['password']
            account.no_telpon = form.cleaned_data['no_telpon']
            account.nik = form.cleaned_data['nik']
            if request.FILES['gambar']:
                account.gambar = request.FILES['gambar']
            account.save(force_update=True)

            return redirect('/account')
        
        return HttpResponse(form.errors)


class DeleteAccountView(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url='/login'
    def get(self, request, id):
        obj = User.objects.get(id=id)
        obj.delete()

        
        return redirect('/account')


class TambahAccountView(LoginRequiredMixin,SuperuserRequiredMixin,View):
    login_url='/login'
    template_name = 'tambah_account.html'

    def get(self, request):
        form =AccountForm(request.POST)
        account = Account.objects.all()

        return render(request, self.template_name, {
            'form': form,
            'account': account,
        })
