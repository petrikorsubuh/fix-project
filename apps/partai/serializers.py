from rest_framework import serializers
from apps.partai import models

class PartaiSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Partai
        fields = '__all__'