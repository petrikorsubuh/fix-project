from rest_framework import serializers
from apps.kelurahan import models
from apps.kecamatan import serializers as serkec


class KelurahanSerializer(serializers.ModelSerializer):
    # kecamatan =serkec.KecamatanSerializer()
    kecamatan = serializers.StringRelatedField()
    class Meta:
        model = models.Kelurahan
        fields=('id','kecamatan', 'nama')