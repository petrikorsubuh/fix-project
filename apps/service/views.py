from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from apps.service import serializers


class TestRespon(views.APIView):

    def get(self, request):

        content = {
            "data": None,
            "detail": "load data gagal",
        }

        return Response(content, status=status.HTTP_200_OK)


class TestUsers(views.APIView):
    
    def get(self, request):
 
        users = User.objects.all()
        serializer = serializers.UsersSerializer(users, many=True)  
        content = {
            "data": serializer.data,
            "detail": "load data gagal",
        }

        return Response(content, status=status.HTTP_200_OK)