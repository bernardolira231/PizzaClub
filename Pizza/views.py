from django.shortcuts import render, redirect
from Pizza.models import Producto
from Pizza.Cart import Carrito

# Create your views here.


def index(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', {
        'productos': productos
    })


def agregarProducto(request, producto_id):
    cart = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    cart.add(producto)


def eliminarProducto(request, producto_id):
    cart = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    cart.delete(producto)


def restarProducto(request, product_id):
    cart = Carrito(request)
    producto = Producto.objects.get(id=product_id)
    cart.restart(producto)


def limpiarCarrito(request):
    cart = Carrito(request)
    cart.clean()


def carrito(request):
    productos = Producto.objects.all()
    return render(request, 'carrito.html', {
        'productos': productos
    })
