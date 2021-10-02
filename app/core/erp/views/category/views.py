from django.shortcuts import render
from core.erp.models import Category, Product
from django.views.generic import ListView


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
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de categorias'
        # context['object_list'] = Product.objects.all()
        return context