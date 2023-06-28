from django.shortcuts import render

# Create your views here.
def home(resquest):
    return render(resquest,'productos/home.html')
def contacto(resquest):
    return render(resquest,'productos/contacto.html')
def nosotros(resquest):
    return render(resquest,'productos/nosotros.html')
def reg(resquest):
    return render(resquest,'productos/reg.html')
def registro(resquest):
    return render(resquest,'productos/registro.html')
def servicios(resquest):
    return render(resquest,'productos/servicios.html')

from django.shortcuts import render, redirect
from .models import Producto, ItemCarrito

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})

def agregar_al_carrito(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    carrito = obtener_carrito(request)
    
    # Verificar si el producto ya está en el carrito
    item_existente = carrito.itemcarrito_set.filter(producto=producto).first()
    if item_existente:
        item_existente.cantidad += 1
        item_existente.subtotal = item_existente.cantidad * producto.precio
        item_existente.save()
    else:
        nuevo_item = ItemCarrito(producto=producto, subtotal=producto.precio)
        carrito.itemcarrito_set.add(nuevo_item)
    
    return redirect('ver_carrito')

def ver_carrito(request):
    carrito = obtener_carrito(request)
    items = carrito.itemcarrito_set.all()
    total = sum(item.subtotal for item in items)
    return render(request, 'carrito.html', {'items': items, 'total': total})

def obtener_carrito(request):
    carrito_id = request.session.get('carrito_id')
    if carrito_id:
        carrito = Carrito.objects.get(id=carrito_id)
    else:
        carrito = Carrito.objects.create()
        request.session['carrito_id'] = carrito.id
    return carrito
