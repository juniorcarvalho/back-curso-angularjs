from django.contrib import admin
from listaTelefonica.core.models import Contato, Operadora


class ContatoModelAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'data', 'operadora']


class OperadoraModelAdmin(admin.ModelAdmin):
    list_display = ['nome', 'codigo', 'categoria', 'preco']

admin.site.register(Contato, ContatoModelAdmin)
admin.site.register(Operadora, OperadoraModelAdmin)
admin.site.site_header = 'Lista Telefônica'