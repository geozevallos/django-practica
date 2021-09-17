from core.erp.views import myFirstView
from django.urls import path

urlpatterns = [
    path('uno/', myFirstView),
    path('dos/', myFirstView),
]