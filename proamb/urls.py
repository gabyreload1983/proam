from .views import send_json
from django.urls import path

from . import views

app_name = 'proamb'
urlpatterns = [
    path('', views.index, name='index'),
    path('granos/', views.granos, name='granos'),
    path('industriahogar/', views.industriahogar, name='industriahogar'),
    path('jardin/', views.jardin, name='jardin'),
    path('maderas/', views.maderes, name='maderes'),
    path('tanques/', views.tanques, name='tanques'),
    path('sendjson/', send_json, name='send_json'),
]
