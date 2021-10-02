from os import name
# from core.erp.views import myFirstView, mySecondView, prueba
from core.erp.views.category.views import CategoryListView, category_list
from django.urls import path

# Especifcinado nombre de las rutas
app_name = 'erp'

# Tambien se puede usar el namespace en el archivo url principal
urlpatterns = [
    # path('uno/', myFirstView, name='vista1'),
    # path('dos/', mySecondView,  name='vista2'),
    # path('tres/', prueba,  name='vista3'),
    # path('category/list/', category_list, name='category_list')
    path('category/list/', CategoryListView.as_view(), name="category_list")
]