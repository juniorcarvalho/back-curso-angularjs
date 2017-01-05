from rest_framework import serializers
from listaTelefonica.core.models import Contato, Operadora


class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        depth = 1
        fields = ['nome', 'telefone', 'data', 'operadora']


class OperadoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operadora
        fields = ['nome', 'codigo', 'categoria', 'preco']
