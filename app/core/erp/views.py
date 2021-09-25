from django.http import HttpResponse, JsonResponse, response
from django.shortcuts import render
from core.erp.models import Category, Product

# Create your views here.

# Vista basada en función
def myFirstView(request):

    data = {
        "name": "Jorge",
        "categories": Category.objects.all()
    }

    # return HttpResponse("Hola, mi primera url :)")
    #retornando json:
    #  return JsonResponse(data)

    #Retornando plantilla: 
    return render(request, 'index.html', data)

def mySecondView(request):

    data = {
        "name": "Jorge",
        "products": Product.objects.all()
    }


    #Retornando plantilla: 
    return render(request, 'second.html', data)

# De prueba
def prueba(request):
    return render(request, 'index.html')