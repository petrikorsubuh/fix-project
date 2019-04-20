from django.shortcuts import render

# Create your views here.
from django.views import View
from apps.caleg import models
from apps.suara import models as ms
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
        values1 =[] #ispartai

        labels = [] #nama caleg
        values = [] #suara caleg

        # val = []

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

        # for s in suara:
        #     t = s


        for c1 in ispartai:
            a1 = c1.suaras
            if tps:
                a1 = a1.filter(tps__id=tps)
            elif kel:
                a1 = a1.filter(kelurahan__id=kel)
            elif kec:
                a1 = a1.filter(kecamatan__id=kec)
            a1 = a1.aggregate(total_suara2=Sum('jumlah_suara'))
            b1 = 0 if a1['total_suara2'] is None else a1['total_suara2']

            a2 = models.Caleg.objects.filter(partai=c1.partai, isprtai=False)
            b2 = 0
            for i in a2:
                a22 = i.suaras
                if tps:
                    a22 = a22.filter(tps__id=tps)
                elif kel:
                    a22 = a22.filter(kelurahan__id=kel)
                elif kec:
                    a22 = a22.filter(kecamatan__id=kec)
                a22 = a22.aggregate(total=Sum('jumlah_suara'))
                a_total = 0 if a22['total'] is None else a22['total']
                b2+=a_total

            b1_2 = b1+b2
            labels1.append(c1.name)
            if b1_2:
                values1.append(b1_2)
            else:
                values1.append(0)
            # values1.append(b1 if b1 else 0)

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

        value_global=[]

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
            a1 = a1.aggregate(total_suara2=Sum('jumlah_suara')) #suara sipartai
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
