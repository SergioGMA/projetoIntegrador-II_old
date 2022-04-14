from django.http import HttpResponse

from .models import Vacina, Profile, Banner
from .serializers import VacinaSerializer, BannerSerializer, ProfileSerializer

from rest_framework import viewsets, mixins
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


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
