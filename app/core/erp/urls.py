from os import name
# from core.erp.views import myFirstView, mySecondView, prueba
from core.erp.views.category.views import CategoryCreateView, CategoryDeleteView, CategoryFormView, CategoryListView, CategoryUpdateView, category_list
from django.urls import path

from core.erp.views.dashboard.views import DashboardView
from core.erp.views.product.views import ProductCreateView, ProductDeleteView, ProductListView, ProductUpdateView
from core.erp.views.test.views import TestView, ReportePersonalizadoExcel
from core.erp.views.client.views import ClientView

# Especifcinado nombre de las rutas
app_name = 'erp'

# Tambien se puede usar el namespace en el archivo url principal
urlpatterns = [
    # path('uno/', myFirstView, name='vista1'),
    # path('dos/', mySecondView,  name='vista2'),
    # path('tres/', prueba,  name='vista3'),
    # path('category/list/', category_list, name='category_list')
    path('category/list/', CategoryListView.as_view(), name="category_list"),
    path('category/add/', CategoryCreateView.as_view(), name="category_add"),
    path('category/edit/<int:pk>/', CategoryUpdateView.as_view(), name="category_edit"),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name="category_delete"),
    path('category/form/', CategoryFormView.as_view(), name="category_form"),
    # product
    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

    # client
    path('client/', ClientView.as_view(), name='client'),

    #Home
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    #Test:
    path('test/', TestView.as_view(), name='test'),    
    path('descarga-excel/', ReportePersonalizadoExcel.as_view(), name='excel'),    
]