from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ProductoForm
from django.http import JsonResponse, HttpResponseForbidden
from django.contrib import messages

def es_superadmin(user):
    return user.is_authenticated and user.rol == "superadmin"


def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'Productos/lista_productos.html', {'productos': productos})


@login_required
def crear_producto(request):
    if not es_superadmin(request.user):
        return redirect('lista_productos')

    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()

    return render(request, 'Productos/crear_producto.html', {'form': form})


@login_required
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    form = ProductoForm(request.POST or None, request.FILES or None, instance=producto)

    if form.is_valid():
        form.save()
        return redirect('lista_productos')

    return render(request, 'Productos/editar_producto.html', {'form': form})


@login_required
def eliminar_producto(request, id):
    if not es_superadmin(request.user):
        return redirect('lista_productos')

    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('lista_productos')


def sobre_nosotros(request):
    return render(request, 'sobre_nosotros.html')


@login_required
def ver_carrito(request):
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    items = CarritoItem.objects.filter(carrito=carrito)
    total = sum(item.total for item in items)
    return render(request, 'carrito.html', {'items': items, 'total': total})


@login_required
def agregar_al_carrito(request, id):
    producto = get_object_or_404(Producto, id=id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    item, created = CarritoItem.objects.get_or_create(carrito=carrito, producto=producto)
    if not created:
        item.cantidad += 1
        item.save()
    messages.success(request, f'{producto.nombre} agregado al carrito.')
    return redirect('lista_productos')


