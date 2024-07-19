"""
URL configuration for drfsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include, re_path
from food.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/listfood/', FoodViewSet.as_view({'get': 'list'})),
    path('api/v1/createfood/', FoodViewSet.as_view({'post': 'create'})),
    path('api/v1/updatefood/<int:pk>/', FoodViewSet.as_view({'put': 'update', 'patch': 'partial_update'})),
    path('api/v1/deletefood/<int:pk>/', FoodViewSet.as_view({'delete': 'destroy'})),

    path('api/v1/createcat/', CategoryViewSet.as_view({'post': 'create'})),
    path('api/v1/listcat/', CategoryViewSet.as_view({'get': 'list'})),
    path('api/v1/updatecat/<int:pk>/', CategoryViewSet.as_view({'put': 'update', 'patch': 'partial_update'})),
    path('api/v1/deletecat/<int:pk>/', CategoryViewSet.as_view({'delete': 'destroy'})),
    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
