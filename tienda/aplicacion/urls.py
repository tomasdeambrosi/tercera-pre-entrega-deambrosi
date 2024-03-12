from django.urls import path, include
from.views import *

urlpatterns = [
    #____________ Menú
    path('', index, name="index"),
    path('articulos/', articulos, name="articulos"),
    path('clientes/', clientes, name="clientes"),
    path('compras/', compras, name="compras"),
    path('ventas/', ventas, name="ventas"),

    #____________ Formularios
    path('articulos_form/', articuloForm, name="articulos_form"),
    path('clientes_form/', clienteForm, name="clientes_form"),
    path('ventas_form/', ventaForm, name="ventas_form"),
    path('compras_form/', compraForm, name="compras_form"),

    #____________ Búsqueda
    path('encontrar_articulos/', encontrarArticulos, name="encontrar_articulos"),
]
