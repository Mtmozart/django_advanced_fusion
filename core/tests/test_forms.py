from django.test import TestCase
from core.forms import ContactForm

class ContactFormTestCase(TestCase):

    def setUp(self):
        self.name = 'Matheus Mozart '
        self.email = 'mmsnborges@gmail.com'
        self.subject = 'teste'
        self.message = 'teste de e-mail'

        self.datas = {
            'name': self.name,
            'email': self.email,
            'subject': self.subject,
            'message': self.message
        }
        self.form = ContactForm(data=self.datas) # igual ContactForm(request.post)

    def test_send_email(self):
        form1 = ContactForm(data=self.datas)
        form1.is_valid()
        res1 = form1.send_mail()

        form2 = self.form
        form2.is_valid()
        res2 = form2.send_mail()

        self.assertEqual(res1, res2)
