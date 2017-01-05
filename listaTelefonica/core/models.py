from django.db import models


class Operadora(models.Model):
    nome = models.CharField(max_length=10, null=True)
    codigo = models.CharField(max_length=2, null=True)
    categoria = models.CharField(max_length=10, null=True)
    preco = models.FloatField(null=True)

    class Meta:
        verbose_name = 'operadora'
        verbose_name_plural = 'operadoras'

    def __str__(self):
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=100, null=True)
    telefone = models.CharField(max_length=10, null=True)
    data = models.DateField(null=True)
    operadora = models.ForeignKey('Operadora')

    class Meta:
        verbose_name = 'contato'
        verbose_name_plural = 'contatos'


