from django.shortcuts import render
from core.erp.models import Category


# Vista basada en funci´no

def category_list(request):
    data = {
        'title': 'Listado de categorias',
        'categories': Category.objects.all()
    }
    return render(request, "category/list.html", data)