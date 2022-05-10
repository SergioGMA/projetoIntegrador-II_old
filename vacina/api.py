from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Vacina, Profile, Banner
from .serializers import VacinaSerializer, BannerSerializer, ProfileSerializer
from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.http.response import JsonResponse
import json

class VacinaViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    authentication_classes = [SessionAuthentication, TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Vacina.objects.none()
    serializer_class = VacinaSerializer

    def get_queryset(self,):
        user = User.objects.get(username=self.request.user)
        queryset = Vacina.objects.all().filter(user=user)
        if queryset.exists():
            return queryset
        else:
            return JsonResponse("/api")


class ProfileViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    authentication_classes = [SessionAuthentication, TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.none()
    serializer_class = ProfileSerializer

    def post(self, request):
        user = User.objects.all().filter(username=request.data['username'])
        prof = Profile.objects.all().filter(cpf=request.data['cpf'])

        if len(user) == 0 and len(prof) == 0:
            u = User.objects.create( username=request.data['username'], password=request.data['password'], )
            u.profile.cpf = request.data['cpf']
            u.profile.first_name = request.data['first_name']
            u.profile.last_name = request.data['last_name']
            u.profile.endereco = request.data['endereco']
            u.profile.telefone = request.data['telefone']
            u.profile.email = request.data['email']
            u.profile.cidade = request.data['cidade']
            u.profile.comorbidade = request.data['comorbidade']
            u.profile.alergia = request.data['alergia']
            u.save()
            return Response({"status": "success", "data": request.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)


class BannerViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    authentication_classes = [SessionAuthentication, TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Banner.objects.none()
    serializer_class = BannerSerializer

    def get_queryset(self,):
        queryset = Banner.objects.all()
        return queryset