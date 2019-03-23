from django.shortcuts import render, redirect
from django.views import View
# Create your views here.


class Index(View):
    template_name = 'public/base.html'

    def get(self, request):

        return render(request, self.template_name
                      )
