from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Tienda, Producto

# Create your views here.

def index(request):
    return render(request, 'index.html')

def registroTienda(request):
    if request.method == 'POST':
        nombreTienda = request.POST.get('nombreTienda')
        fechaCreacion = request.POST.get('fechaTienda')
        direccion = request.POST.get('direccionTienda')
        provincia = request.POST.get('provinciaTienda')
        region = request.POST.get('regionTienda')
        telefonoContacto = request.POST.get('telefonoTienda')
        Tienda.objects.create(
            nombreTienda=nombreTienda,
            fechaCreacion=fechaCreacion,
            direccion = direccion,
            provincia = provincia,
            telefonoContacto = telefonoContacto,
            region = region
        )
        return HttpResponseRedirect(reverse('gestionTienda:registroTienda'))
    return render(request,'registroTienda.html',{
        'tiendaTotales':Tienda.objects.all().order_by('id'),
    })

def eliminarTienda(request,idTienda):
    tiendaEliminar = Tienda.objects.get(id=idTienda)
    tiendaEliminar.delete()
    return HttpResponseRedirect(reverse('gestionTienda:registroTienda'))

def Productos(request):
    if request.method == 'POST':
        nombreProducto = request.POST.get('nombreProductos')
        descripcion = request.POST.get('descripcionProductos')
        codigo = request.POST.get('codigoProductos')
        precioVenta = request.POST.get('precioProductos')
        cantidad = request.POST.get('cantidadProductos')
        Producto.objects.create(
            nombreProducto=nombreProducto,
            descripcion=descripcion,
            codigoProducto = codigo,
            precioVenta = precioVenta,
            cantidad = cantidad
        )
        return HttpResponseRedirect(reverse('gestionTienda:Productos'))
    return render(request,'Productos.html',{
        'productoTotales':Producto.objects.all().order_by('id'),
        'tiendaTotales':Tienda.objects.all().order_by('id'),
    })

def eliminarProducto(request,idProducto):
    productoEliminar = Producto.objects.get(id=idProducto)
    productoEliminar.delete()
    return HttpResponseRedirect(reverse('gestionTienda:Productos'))

def asignarProducto(request):
    if request.method == 'POST':
        idProducto = request.POST.get('productoSeleccionado')
        idTienda = request.POST.get('tiendaSeleccionado')
        objectoProducto = Producto.objects.get(id=idProducto)
        objectoTienda = Tienda.objects.get(id=idTienda)
        objectoProducto.tiendaR = objectoTienda
        objectoProducto.save()
    return HttpResponseRedirect(reverse('gestionTienda:Productos'))

def verProductosTienda(request, idTienda):
    tiendaSeleccionada = Tienda.objects.get(id=idTienda)
    productosTienda = Producto.objects.filter(tiendaR=tiendaSeleccionada)
    return render(request, 'verProductosTienda.html', {'tiendaSeleccionada': tiendaSeleccionada, 'productosTienda': productosTienda})

