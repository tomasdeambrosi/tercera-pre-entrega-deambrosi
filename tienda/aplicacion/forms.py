from django import forms

class ArticuloForm(forms.Form):
    nombre = forms.CharField(max_length=60, required=True)
    categoria = forms.CharField(max_length=60, required=True)
    precio_compra = forms.FloatField(required=True)
    precio_venta = forms.FloatField(required=True)

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=60, required=True)
    apellido = forms.CharField(max_length=60, required=True) 
    telefono = forms.CharField(max_length=15, required=True)   

class VentaForm(forms.Form):
    articulo = forms.CharField(max_length=60, required=True) 
    cantidad = forms.IntegerField(required=True)

class CompraForm(forms.Form):
    distribuidor = forms.CharField(max_length=60, required=True)
    articulo = forms.CharField(max_length=60, required=True) 
    cantidad = forms.IntegerField(required=True)