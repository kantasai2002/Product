"""
URL configuration for sbadmin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from sbadminapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('customer/insert',views.insert,name='insert'),
    path('customer/insert1',views.insert1,name='insert1'),
    path('customer/listcust',views.listcust,name='listcust'),
    path('customer/dele/<int:id>',views.dele,name='dele'),
    path('customer/edit/<int:id>',views.edit,name='edit'),
    path('customer/update/<int:id>',views.update,name='edit'),
]
