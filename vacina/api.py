from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import Vacina, Profile, Banner
from .serializers import VacinaSerializer, BannerSerializer, ProfileSerializer

from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

import json

class VacinaViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Vacina.objects.none()
    serializer_class = VacinaSerializer

    def get_queryset(self,):
        queryset = Vacina.objects.all()
        return queryset


    def post(self, request, *args, **kwargs):
        try:
            print(request.body)
            if len(request.body) > 0:
                data = json.loads(request.body)
                d = Vacina(user=data['user'], vacina=data['vacina'], fabricante=data['fabricante'], lote=data['lote'], dose=data['dose'], prof=data['prof'], reg_profissional=data['reg_profissional'], unidade=data['unidade'], data_aplicacao=data['data_aplicacao'], data_fabricacao=data['data_fabricacao'], data_validade=data['data_validade'])
                d.save()
                return Response({'status': True, 'msg':'ok'})
            else:
                return Response({'status': False, 'msg':'data invalid'})

        except Exception as error:
            return HttpResponse(error)



class ProfileViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Profile.objects.none()
    serializer_class = ProfileSerializer

    def post(self, request):
        user = User.objects.all().filter(username=request.data['username'])
        prof = Profile.objects.all().filter(cpf=request.data['cpf'])

        if len(user) == 0 and len(prof) == 0:
            u = User.objects.create( username=request.data['username'], password=request.data['password'], )
            u.profile.cpf = request.data['cpf']
            u.profile.telefone = request.data['telefone']
            u.profile.telefone = request.data['telefone']
            u.profile.telefone = request.data['telefone']
            u.profile.telefone = request.data['telefone']
            u.save()
            return Response({"status": "success", "data": request.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)


class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
