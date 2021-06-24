from django.shortcuts import render, redirect
from sitio import views
from .carro import Carro
from django.http import HttpResponse, HttpResponseBadRequest
import requests


# Create your views here.

def agregar_producto(request, producto_id):
    
    response = requests.get('http://54.226.41.225:8000/productos').json()
        
    for obj in response:
        
        if obj['cod_prod'] == producto_id:
            producto = [obj['cod_prod'], obj['descripcion'], obj['pr_venta'], obj['imagen']]
    
    #print(producto[0])
    carro=Carro(request)
    carro.agregar(producto=producto)
    return redirect("sitio")

def eliminar_producto(request, producto_id):
    #response = requests.get('http://54.175.6.198:8000/productos').json()
        
    #for obj in response:
        
    #    if obj['cod_prod'] == producto_id:
    #        producto = [obj['cod_prod'], obj['descripcion'], obj['pr_venta'], obj['imagen']]
    carro=Carro(request)
    #producto= Producto.objects.get(id=producto_id)
     
    carro.eliminar(producto=producto_id)
    return redirect("sitio")

def restar_producto(request, producto_id):
    response = requests.get('http://54.226.41.225:8000/productos').json()
        
    for obj in response:
        #print(obj['cod_prod'])
        if obj['cod_prod'] == str(producto_id):

            producto = [obj['cod_prod'], obj['descripcion'], obj['pr_venta'], obj['imagen']]
            print (producto[0])

    carro=Carro(request)
    carro.restar_producto(producto=producto)
    return redirect("sitio")

def limpiar_carro(request, producto_id):

    carro=Carro(request)
    carro.limpiar_carro()
    return redirect("sitio")