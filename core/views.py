from django.views.generic import FormView
from .models import Service, Employee, Resources
from .forms import ContactForm
from django.urls import reverse_lazy
from django.contrib import messages

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        #recuperação de contexto
        context = super(IndexView, self).get_context_data(*kwargs)
        #adcionar novos contextos
        context['services'] = Service.objects.order_by('?').all()
        context['employee'] = Employee.objects.order_by('?').all()
        context['resources'] = Resources.objects.order_by('?').all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar o e-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)

