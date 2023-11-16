from django.shortcuts import render, redirect
from .models import Producto
from .forms import ClienteForm, PedidoForm

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'tiendafika/lista_productos.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    return render(request, 'tiendafika/detalle_producto.html', {'producto': producto})

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes') # Cambia el nombre de la vista
    else:
        form = ClienteForm()
    return render(request, 'tiendafika/crear_cliente.html', {'form': form})

def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos') # Cambia el nombre de la vista
    else:
        form = PedidoForm()
    return render(request, 'tiendafika/crear_pedido.html', {'form': form})

