import uuid
from django.test import TestCase
from model_mommy import mommy

from core.models import get_file_path

class GetFilePathTestCase(TestCase):

    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'

    def test_get_file_path(self):
        arquivo = get_file_path(None, 'teste.png')
        self.assertTrue(len(arquivo), len(self.filename))

class ServiceTestCase(TestCase):
    
    def setUp(self):
        self.service = mommy.make('Service')

    def test_str(self):
        self.assertEquals(str(self.service), self.service.service)


class JobTitleTestCase(TestCase):

    def setUp(self):
        self.job_title = mommy.make('JobTitle')

    def test_str(self):
        self.assertEquals(str(self.job_title), self.job_title.job_title)

class EmployeeTestCase(TestCase):

    def setUp(self):
        self.employee = mommy.make('Employee')

    def test_str(self):
        self.assertEquals(str(self.employee), self.employee.name)