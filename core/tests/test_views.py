from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.datas = {
            'name': 'Scarllet',
            'email': 'viuvanegra@gmail.com',
            'subject': 'Meu assunto',
            'message': 'Minha mensagem'
        }
        self.clent = Client()

    def test_form_valid(self):
        request = self.clent.post(reverse_lazy('index'), data=self.datas)
        self.assertEquals(request.status_code, 302)

    def test_form_invalid(self):
        datas = {
            'name': 'Scarllet',
            'subject': 'Meu assunto'
        }
        request = self.clent.post(reverse_lazy('index'), data=datas)
        self.assertEquals(request.status_code, 200)
