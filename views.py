from django.shortcuts import render
from .models import Producto
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'app/index.html')

def tienda(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request,'app/tienda.html', data)

def carrito(request):
    return render(request,'app/carrito.html')


def detalle(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request,'app/detalle.html', data)


    
