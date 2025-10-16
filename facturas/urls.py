from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_facturas, name='lista_facturas'),
    path('factura/nueva/', views.nueva_factura, name='nueva_factura'),
    path('factura/<int:pk>/', views.factura_detalle, name='factura_detalle'),
]