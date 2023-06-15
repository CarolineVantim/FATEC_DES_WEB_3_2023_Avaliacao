from django.test import TestCase
from .models import CadastroModel
from django.utils import timezone

class CadastroModelTest(TestCase):
    
    def setUp(self):
        self.cadastro = CadastroModel.objects.create(
            nome='Aluno Teste',
            professor='Orlando',
            data=timezone.now())

    def test_str(self):
        self.assertEqual(str(self.cadastro), 'Aluno Teste')

    def test_status_code_list(self):
        response = self.client.get('/listar')
        self.assertEqual(response.status_code, 200)
    
    def test_status_code_register(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)