"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from core.erp.views import myFirstView
from django.contrib import admin
from django.urls import path, include
from core.homepage.views import IndexView
from core.login.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('primeraurl/', include('core.erp.urls'))
    path('erp/', include('core.erp.urls')),
    path('', IndexView.as_view(), name='homepage'),
    path('login/', LoginFormView2.as_view(), name='login'),
    # path('logout/', LogoutView.as_view()),
    path('logout/', LogoutRedirectView.as_view(), name='logout'),
]
