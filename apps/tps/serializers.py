from rest_framework import serializers
from apps.tps import models
from apps.kelurahan.serializers import KelurahanSerializer
from apps.kelurahan.models import Kelurahan


class TpsSerializer(serializers.ModelSerializer):
    kelurahan = KelurahanSerializer()

    class Meta:
        model = models.Tps
        fields = ('id', 'kelurahan', 'alamat', 'nama')

    def create(self, validated_data):
        kelurahan_data = validated_data.pop("kelurahan", None)
        if kelurahan_data:
            kelurahan = Kelurahan.objects.get_or_create(**kelurahan_data)[0]
            # print(kelurahan)
            validated_data["kelurahan"] = kelurahan
            # print(validated_data["kelurahan"])
        return models.Tps.objects.create(**validated_data)
