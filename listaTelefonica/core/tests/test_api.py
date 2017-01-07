from rest_framework import status
from rest_framework.test import APITestCase
from listaTelefonica.core.models import Contato, Operadora


class testOperadora(APITestCase):
    def setUp(self):
        self.url = '/operadora/'
        self.operadora = {"id": 1, "nome": "Oi", "codigo": "31", "categoria": "Celular", "preco": 0.25}

    def test_status_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_operadora(self):
        self.response = self.client.post(self.url, self.operadora, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Operadora.objects.count(), 1)
        self.assertEqual(Operadora.objects.get().nome, 'Oi')

    def test_list_operadora(self):
        self.client.post(self.url, self.operadora)
        response = self.client.get(self.url)
        # self.assertEqual(loads(dumps(response.data)), self.operadora)
        self.assertEqual(response.data, self.operadora)


class testContato(APITestCase):
    def setUp(self):
        self.url = '/contato/'
        self.operadora = {"id": 1, "nome": "Oi", "codigo": "31", "categoria": "Celular", "preco": 0.25}
        self.contato = {"id": 1, "nome": "Pedro", "telefone": "99999-9999", "data": "2017-01-04",
                        "operadora": self.operadora}
        self.client.post('/operadora/', self.operadora, format='json')

    def test_status_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_contato(self):
        response = self.client.post(self.url, self.contato, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Contato.objects.count(), 1)
        self.assertEqual(Contato.objects.get().nome, 'Pedro')

    def test_delete_contato(self):
        self.client.post(self.url, self.contato, format='json')
        response = self.client.delete('/contato/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # def test_delete_contato_not_found(self):
    #     response = self.client.delete('/contatoDelete/999/', format='json')
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
