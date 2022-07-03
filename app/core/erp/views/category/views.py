from django.http import JsonResponse
from django.shortcuts import render
from core.erp.models import Category, Product
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
import json

# Vista basada en funci´no

def category_list(request):
    data = {
        'title': 'Listado de categorias',
        'categories': Category.objects.all()
    }
    return render(request, "category/list.html", data)


class CategoryListView(ListView):
    #Tengo que decirle cual es el modelo
    model = Category

    #Cual es la plantilla
    template_name = 'category/list.html'

    # def get_queryset(self):
    #     return Category.objects.filter(name__startswith = 'B')

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        data = {}
        # post_data = json.loads(request.body.decode("utf-8")) # usando FetchAPI
        post_data = request.POST #Usando Jquery}
        try:
            data = Category.objects.get(pk=post_data['id'])
            data = data.toJSON()
        except Exception as e:
            data['error']=str(e)

        return JsonResponse(data)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de categorias'
        # context['object_list'] = Product.objects.all()
        return context