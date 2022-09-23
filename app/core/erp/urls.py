from os import name
# from core.erp.views import myFirstView, mySecondView, prueba
from core.erp.views.category.views import CategoryCreateView, CategoryDeleteView, CategoryFormView, CategoryListView, CategoryUpdateView, category_list
from django.urls import path

from core.erp.views.dashboard.views import DashboardView

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
    #Home
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]