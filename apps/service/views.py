from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from apps.dapil.models import Dapil
from apps.account.models import Account
from apps.partai.models import Partai
from apps.caleg.models import Caleg
from apps.kategori.models import KategoriCaleg
from apps.kecamatan.models import Kecamatan
from apps.kelurahan.models import Kelurahan
from apps.suara.models import Suara
from apps.service import serializers


class ApiRespon(views.APIView):

    def get(self, request):

        content = {
            "data": None,
            "detail": "load data gagal",
        }

        return Response(content, status=status.HTTP_200_OK)


class ApiUsers(views.APIView):
    
    def get(self, request):
 
        users = User.objects.all()
        serializer = serializers.UsersSerializer(users, many=True)  
        content = {
            "data": serializer.data,
            "detail": "load data gagal",
        }

        return Response(content, status=status.HTTP_200_OK)

class ApiDapil(views.APIView):

    def get(self,request):

        dapils = Dapil.objects.all()
        serializer = serializers.DapilSerializer(dapils, many=True)
        content = {
            "data":serializer.data,
            "detail": "load data gagal"
        }

        return Response(content, status=status.HTTP_200_OK)


class ApiAccount(views.APIView):

    def get(self, request):

        accounts = Account.objects.all()
        serializer = serializers.AccountSerialzer(accounts, many=True)
        content = {
            "data":serializer.data,
            "detail":"load data gagal"
        }

        return Response(content, status=status.HTTP_200_OK)

class ApiPartai(views.APIView):

    def get(Self, request):

        partais = Partai.objects.all()
        serializer = serializers.PartaiSerilizer(partais, many=True)
        content = {
            "data":serializer.data,
        }

        return Response(content, status=status.HTTP_200_OK)


class ApiCaleg(views.APIView):

    def get(self, request):

        calegs = Caleg.objects.all()
        serializer = serializers.CalegSerializer(calegs, many=True)
        content = {
            "data":serializer.data,
        }

        return Response(content, status=status.HTTP_200_OK)


class ApiKategori(views.APIView):

    def get(self, request):
        kategoris = KategoriCaleg.objects.all()
        serializer = serializers.KategoriCalegSerializer(kategoris, many=True)
        content = {
            "data":serializer.data,
        }

        return Response(content,status=status.HTTP_200_OK)


class ApiKecamatan(views.APIView):

    def get(self, request):
        kecamatans = Kecamatan.objects.all()
        serializer = serializers.KecamatanSerializerci(kecamatans, many=True)
        content = {
            "data":serializer.data,
        }

        return Response(content,status=status.HTTP_200_OK)


class ApiKelurahan(views.APIView):
    
    def get(self, request):
        kelurahans = Kelurahan.objects.all()
        serializer = serializers.KelurahanSerializer(kelurahans, many=True)
        content ={
            "data":serializer.data,
        }

        return Response(content,status=status.HTTP_200_OK)


class ApiSuara(views.APIView):
    
    def get(self, request):
        suaras = Suara.objects.all()
        serializer = serializers.SuaraSerializer(suaras, many=True)
        content ={
            "data":serializer.data,
        }

        return Response(content,status=status.HTTP_200_OK)