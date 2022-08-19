from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from core.erp.models import Category, Product
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt
import json

from core.erp.views.category.forms import CategoryForm

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
        context['create_url']=reverse_lazy('erp:category_add')
        context['list_url']=reverse_lazy('erp:category_list')
        context['entity']='Category'
        return context

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name ="category/create.html"
    success_url= reverse_lazy('erp:category_list')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                # form = CategoryForm(request.POST)
                form = self.get_form()
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha ingresado una accion'
        except Exception as e:
                data['error']=str(e)

        return JsonResponse(data)


    #Data adicional a mandar
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear categoría'
        context['list_url']=reverse_lazy('erp:category_list')
        context['entity']='Category'
        context['action']='add'
        return context

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name ="category/create.html"
    success_url= reverse_lazy('erp:category_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                # form = CategoryForm(request.POST)
                form = self.get_form()
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha ingresado una accion'
        except Exception as e:
                data['error']=str(e)

        return JsonResponse(data)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar categoría'
        context['list_url']=reverse_lazy('erp:category_list')
        context['entity']='Category'
        context['action']='edit'
        return context


class  CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category/delete.html'
    success_url = reverse_lazy('erp:category_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e: 
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar categoría'
        context['list_url']=reverse_lazy('erp:category_list')
        context['entity']='Category'
        return context