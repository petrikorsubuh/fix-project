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

        tps = request.GET.get("tps", None)
        kel = request.GET.get("kel", None)
        kec = request.GET.get("kec", None)

        labels1 = []
        values1 =[]

        labels = []
        values = []


        for c in caleg:
            a = c.suaras
            if tps:
                a = a.filter(tps__id=tps)
            elif kel:
                a = a.filter(kelurahan__id=kel)
            elif kec:
                a = a.filter(kecamatan__id=kec)
            a = a.aggregate(total_suara=Sum('jumlah_suara'))
            b = a['total_suara']

            labels.append(c.name)
            values.append(b if b else 0)

        for c1 in ispartai:
            a1 = c1.suaras
            if tps:
                a1 = a1.filter(tps__id=tps)
            elif kel:
                a1 = a1.filter(kelurahan__id=kel)
            elif kec:
                a1 = a1.filter(kecamatan__id=kec)
            a1 = a1.aggregate(total_suara2=Sum('jumlah_suara'))
            b1 = a1['total_suara2']

            labels1.append(c1.name)
            # if b:
            #     values1.append(b1)
            # else:
            #     values1.append(0)
            values1.append(b1 if b1 else 0)

        return render(request, self.template_name, {
            'values': values,
            'labels': labels,
            'values1': values1,
            'labels1': labels1,
        })


class ChartAdmin(View):
    template_name = 'chart.html'
    def get(self, request):

        caleg = models.Caleg.objects.filter(partai__name='DEMOKRAT').all()
        ispartai = models.Caleg.objects.filter(isprtai=True)

        tps = request.GET.get("tps", None)
        kel = request.GET.get("kel", None)
        kec = request.GET.get("kec", None)

        labels1 = []
        values1 =[]

        labels = []
        values = []


        for c in caleg:
            a = c.suaras
            if tps:
                a = a.filter(tps__id=tps)
            elif kel:
                a = a.filter(kelurahan__id=kel)
            elif kec:
                a = a.filter(kecamatan__id=kec)
            a = a.aggregate(total_suara=Sum('jumlah_suara'))
            b = a['total_suara']

            labels.append(c.name)
            values.append(b if b else 0)

        for c1 in ispartai:
            a1 = c1.suaras
            if tps:
                a1 = a1.filter(tps__id=tps)
            elif kel:
                a1 = a1.filter(kelurahan__id=kel)
            elif kec:
                a1 = a1.filter(kecamatan__id=kec)
            a1 = a1.aggregate(total_suara2=Sum('jumlah_suara'))
            b1 = a1['total_suara2']

            labels1.append(c1.name)
            # if b:
            #     values1.append(b1)
            # else:
            #     values1.append(0)
            values1.append(b1 if b1 else 0)

        return render(request, self.template_name, {
            'values': values,
            'labels': labels,
            'values1': values1,
            'labels1': labels1,
        })
