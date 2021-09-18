from os import name
from core.erp.views import myFirstView, mySecondView
from django.urls import path

# Especifcinado nombre de las rutas
app_name = 'erp'

# Tambien se puede usar el namespace en el archivo url principal
urlpatterns = [
    path('uno/', myFirstView, name='vista1'),
    path('dos/', mySecondView,  name='vista2'),
]