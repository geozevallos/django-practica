from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from core.erp.models import Client
from core.erp.forms import ClientForm


class ClientView(TemplateView):
    template_name = 'client/list.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Client.objects.all():
                    data.append(i.toJSON())
            elif action == "add":
                cliente = Client()
                cliente.names = request.POST['names']
                cliente.surnames = request.POST['surnames']
                cliente.dni = request.POST['dni']
                cliente.address = request.POST['address']
                cliente.gender = request.POST['gender']
                cliente.save()
            elif action == "edit":
                cliente = Client.objects.get(pk=request.POST['id'])
                cliente.names = request.POST['names']
                cliente.surnames = request.POST['surnames']
                cliente.dni = request.POST['dni']
                cliente.address = request.POST['address']
                cliente.gender = request.POST['gender']
                cliente.save()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Clientes'
        context['list_url'] = reverse_lazy('erp:client')
        context['entity'] = 'Clientes'
        context['form'] = ClientForm()
        return context