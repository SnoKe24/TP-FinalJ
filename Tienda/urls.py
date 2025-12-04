from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name="lista_productos"),
    path('crear/', views.crear_producto, name="crear_producto"),
    path('editar/<int:id>/', views.editar_producto, name="editar_producto"),
    path('eliminar/<int:id>/', views.eliminar_producto, name="eliminar_producto"),
    path('sobre-nosotros/', views.sobre_nosotros, name="sobre_nosotros"),
    path('carrito/', views.ver_carrito, name="ver_carrito"),
    path('agregar-al-carrito/<int:id>/', views.agregar_al_carrito, name="agregar_al_carrito"),

]
