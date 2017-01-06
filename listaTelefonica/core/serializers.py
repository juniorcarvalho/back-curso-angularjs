from rest_framework import serializers
from listaTelefonica.core.models import Contato, Operadora


class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = ['id', 'nome', 'telefone', 'data', 'operadora']
        depth = 1

class OperadoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operadora
        fields = ['id', 'nome', 'codigo', 'categoria', 'preco']
