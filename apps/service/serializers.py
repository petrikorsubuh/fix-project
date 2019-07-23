from rest_framework import serializers
from django.contrib.auth.models import User
from apps.dapil.models import Dapil
from apps.account.models import Account
from apps.partai.models import Partai
from apps.caleg.models import Caleg
from apps.kategori.models import KategoriCaleg
from apps.kecamatan.models import Kecamatan
from apps.kelurahan.models import Kelurahan
from apps.suara.models import Suara

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','id')


class DapilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dapil
        fields = ('name','alamat')

class AccountSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('user', 'name', 'no_telpon', 'nik', 'gambar')

class PartaiSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Partai
        fields = ('name', 'no_urut', 'gambar')


class CalegSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caleg
        fields = ('name', 'nomor_urut', 'dapil', 'partai', 'kategoricaleg', 'isprtai')


class KategoriCalegSerializer(serializers.ModelSerializer):
    class Meta:
        model = KategoriCaleg
        fields = "__all__"


class KecamatanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kecamatan
        fields = "__all__"

class KelurahanSerializer(serializers.ModelSerializer):
    class Meta:
        model =Kelurahan
        fields = "__all__"

class SuaraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suara
        fields = "__all__"