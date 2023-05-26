from django.views.generic import TemplateView

from .models import Service, Employee, Resources

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        #recuperação de contexto
        context = super(IndexView, self).get_context_data(*kwargs)
        #adcionar novos contextos
        context['services'] = Service.objects.order_by('?').all()
        context['employee'] = Employee.objects.order_by('?').all()
        context['resources'] = Resources.objects.order_by('?').all()
        return context


