from django.conf.urls import url
from django.contrib import admin
from listaTelefonica.core.views import contato_api, operadora_api

urlpatterns = [

    url(r'^', admin.site.urls),
    url(r'^contato/$', contato_api),
    url(r'^contato/(?P<pk>\d+)', contato_api),
    url(r'^operadora/$', operadora_api),
]
