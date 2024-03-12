from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, "aplicacion/index.html")

def articulos(request):
    contexto = {'articulos': Articulo.objects.all()}
    return render(request, "aplicacion/articulos.html", contexto)

def clientes(request):
    contexto = {'clientes': Cliente.objects.all()}
    return render(request, "aplicacion/clientes.html", contexto)

def ventas(request):
    contexto = {'ventas': Venta.objects.all()}
    return render(request, "aplicacion/ventas.html", contexto)

def compras(request):
    contexto = {'compras': Compra.objects.all()}
    return render(request, "aplicacion/compras.html", contexto)

#____________________ Forms

def articuloForm(request):

    if request.method == "POST":
        miForm = ArticuloForm(request.POST)
        if miForm.is_valid():
            articulo_nombre = miForm.cleaned_data.get("nombre")
            articulo_categoria = miForm.cleaned_data.get("categoria")
            articulo_precio_compra = miForm.cleaned_data.get("precio_compra")
            articulo_precio_venta = miForm.cleaned_data.get("precio_venta")
            articulo = Articulo(nombre=articulo_nombre, categoria=articulo_categoria, precio_compra=articulo_precio_compra, precio_venta=articulo_precio_venta)
            articulo.save()
            
            contexto = {'articulos': Articulo.objects.all()}
            return render(request, "aplicacion/articulos.html", contexto)
    else:
       miForm = ArticuloForm()
    
    return render(request, "aplicacion/articulos_form.html", {"form": miForm})


def clienteForm(request):
    
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            cliente_nombre = miForm.cleaned_data.get("nombre")
            cliente_apellido = miForm.cleaned_data.get("apellido")
            cliente_telefono = miForm.cleaned_data.get("telefono")
            cliente = Cliente(nombre=cliente_nombre, apellido=cliente_apellido, telefono=cliente_telefono)
            cliente.save()
            
            contexto = {'clientes': Cliente.objects.all()}
            return render(request, "aplicacion/clientes.html", contexto)
    else:
       miForm = ClienteForm()
    
    return render(request, "aplicacion/clientes_form.html", {"form": miForm})


def ventaForm(request):
    
    if request.method == "POST":
        miForm = VentaForm(request.POST)
        if miForm.is_valid():
            venta_articulo = miForm.cleaned_data.get("articulo")
            venta_cantidad = miForm.cleaned_data.get("cantidad")
            venta = Venta(articulo=venta_articulo, cantidad=venta_cantidad)
            venta.save()
            
            contexto = {'ventas': Venta.objects.all()}
            return render(request, "aplicacion/ventas.html", contexto)
    else:
       miForm = VentaForm()
    
    return render(request, "aplicacion/ventas_form.html", {"form": miForm})


def compraForm(request):
    
    if request.method == "POST":
        miForm = CompraForm(request.POST)
        if miForm.is_valid():
            compra_distribuidor = miForm.cleaned_data.get("distribuidor")
            compra_articulo = miForm.cleaned_data.get("articulo")
            compra_cantidad = miForm.cleaned_data.get("cantidad")
            compra = Compra(distribuidor=compra_distribuidor, articulo=compra_articulo, cantidad=compra_cantidad)
            compra.save()
            
            contexto = {'compras': Compra.objects.all()}
            return render(request, "aplicacion/compras.html", contexto)
    else:
       miForm = CompraForm()
    
    return render(request, "aplicacion/compras_form.html", {"form": miForm})


#____________________ Búsqueda

def buscarArticulos(request):
    return render(request, "aplicacion/index.html")

def encontrarArticulos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        articulos = Articulo.objects.filter(nombre__icontains=patron)
        contexto = {"articulos": articulos}
        return render(request, "aplicacion/articulos.html", contexto)

    contexto = {'articulos': Articulo.objects.all()}
    return render(request, "aplicacion/articulos.html", contexto)