from django.shortcuts import render

# Create your views here.
from django.views import View
from apps.caleg import models
from django.db.models import Sum

class ChartPublic(View):
    template_name = 'public/base.html'
    def get(self, request):

        caleg = models.Caleg.objects.filter(partai__name='DEMOKRAT').all()
        ispartai = models.Caleg.objects.filter(isprtai=True)

        labels1 = []
        values1 =[]

        labels = []
        values = []


        for c in caleg:
            a = c.suaras.aggregate(total_suara=Sum('jumlah_suara'))
            b = a['total_suara']

            labels.append(c.name)
            values.append(b)

        for c1 in ispartai:
            a1 = c1.suaras.aggregate(total_suara2=Sum('jumlah_suara'))
            b1 = a1['total_suara2']

            labels1.append(c1.name)
            values1.append(b1)

        return render(request, self.template_name, {
            'values': values,
            'labels': labels,
            'values1': values1,
            'labels1': labels1,
        })
