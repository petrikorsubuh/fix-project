from rest_framework import serializers
from apps.caleg import models

class CalegSerializer(serializers.ModelSerializer):
    partai = serializers.StringRelatedField()
    dapil = serializers.StringRelatedField()
    kategoricaleg = serializers.StringRelatedField()
    class Meta:
        model = models.Caleg
        fields = ('name','id','partai','dapil','kategoricaleg')