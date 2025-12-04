from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Producto
from .forms import ProductoForm
from django.http import HttpResponseForbidden

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
