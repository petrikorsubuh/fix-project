from django.shortcuts import render, redirect
from django.views import View
from apps.authentication import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from apps.account import models
# Create your views here.


class LoginView(View):
    template_name = 'auth/login.html'

    def get(self, request):

        return render(request, self.template_name)


class LoginProccessView(View):
    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user:
                if hasattr(user, 'account'):
                    if user.is_superuser:
                        login(request, user)
                        return redirect('/caleg')
                    elif user.is_staff:
                        login(request, user)
                        return redirect('/relawan')

                messages.error(
                    request, 'Akun tidak diizinkan untuk mengakses halaman ini')
                return redirect('/login')

            messages.error(
                request, 'Username dan password tidak ditemukan')
            return redirect('/login')

        messages.error(request, 'Form harus di isi')
        return redirect('/login')


class LogOutView(View):
    def get(self, request):
        logout(request)

        return redirect('/login')
