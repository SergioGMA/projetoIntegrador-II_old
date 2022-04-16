from rest_framework import serializers
from .models import Vacina, Profile, Banner


class VacinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacina
        fields = [
            'id',
            'user', 
            'vacina', 
            'fabricante', 
            'lote', 
            'dose', 
            'prof',
            'reg_profissional',
            'unidade',
            'data_fabricacao',
            'data_validade',
            ]


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'id',
            'user', 
            'first_name', 
            'last_name', 
            'endereco', 
            'telefone', 
            'email',
            'cidade',
            'Comorbidade', 
            'alergia', 
            'cpf',
            'password',
            'confirm',
        ]


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = [
            'id',
            'banner',
        ]