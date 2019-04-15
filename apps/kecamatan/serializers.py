from rest_framework import serializers
from apps.kecamatan import models

class KecamatanSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Kecamatan
        fields = '__all__'