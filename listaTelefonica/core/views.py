from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from listaTelefonica.core.models import Contato, Operadora
from listaTelefonica.core.serializers import ContatoSerializer, OperadoraSerializer


@api_view(['GET', 'POST', 'DELETE'])
def contato_api(request, pk=None):
    if request.method == 'GET':
        contatos = Contato.objects.all()
        serializer = ContatoSerializer(contatos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ContatoSerializer(data=request.data)
        if serializer.is_valid():
            try:
                op = Operadora.objects.get(pk=int(request.data['operadora']['id']))
            except Operadora.DoesNotExists:
                op = None
            if op:
                serializer.save(operadora=op)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        try:
            contato = Contato.objects.get(pk=pk)
        except Contato.DoesNotExists:
            contato = None
        if contato:
            contato.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def operadora_api(request):
    if request.method == 'GET':
        operadoras = Operadora.objects.all()
        serializer = OperadoraSerializer(operadoras, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = OperadoraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
