from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ProductoForm
from django.http import JsonResponse, HttpResponseForbidden

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
    if not es_superadmin(request.user):
        return redirect('lista_productos')

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

def obtener_carrito(usuario):
    carrito, creado = Carrito.objects.get_or_create(usuario=usuario)
    return carrito

@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)

    item, creado_item = CarritoItem.objects.get_or_create(
        carrito=carrito,
        producto=producto
    )

    if not creado_item:
        item.cantidad += 1
        item.save()

    # devolver solo el HTML parcial
    return render(request, 'Tienda/carrito_parcial.html', {'carrito': carrito})

@login_required
def carrito_parcial(request):
    carrito = obtener_carrito(request.user)
    return render(request, "Tienda/carrito_parcial.html", {"carrito": carrito})

@login_required
def ver_carrito(request):
    carrito = obtener_carrito(request.user)
    return render(request, "Tienda/carrito.html", {"carrito": carrito})
