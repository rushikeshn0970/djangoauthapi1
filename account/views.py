# from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.serializers import UserRegistrationSerializer
from rest_framework import generics

class UserRegistrationView(APIView):
    def post(self, request, format=None):
        try:
            serializer= UserRegistrationSerializer(data=request.data)
        except Exception as g:
            serializer=None
            print(g)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({ 'msg' :' Registration Success'},
            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)