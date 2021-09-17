from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

# Vista basada en función
def myFirstView(request):
    data = {
        "name": "Jorge"
    }
    # return HttpResponse("Hola, mi primera url :)")
    return JsonResponse(data)