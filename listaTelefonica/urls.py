from django.conf.urls import url
from django.contrib import admin
from listaTelefonica.core.views import contato_api, operadora_api, contato_api_delete

urlpatterns = [

    url(r'^', admin.site.urls),
    url(r'^contato/$', contato_api),
    url(r'^operadora/$', operadora_api),
    url(r'^contatoDelete/(?P<pk>\d+)', contato_api_delete),
]
