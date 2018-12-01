from django.shortcuts import render
from django.http import HttpResponse
from .models import Adoptante
import requests

# Create your views here.


def index(request):
    response = requests.get('http://api.ipstack.com/201.214.154.159?access_key=af0a4628af41d8a86c1641f035bebe91')
    data = response.json()
    return render(request, 'index.html',{'nombre': "Marcelo", 'elementos':Adoptante.objects.all(),'ip': data['ip'],'país':data['country_name'],'ciudad': data['city'],'region': data['region_code'],'continente': data['continent_name']})


def registro(request):
    return render(request,'formulario.html',{})


def crear(request):
    correo = request.POST.get('email',0)
    run = request.POST.get('rut',0)
    nombre = request.POST.get('nombre',0)
    fechan = request.POST.get('fecha_n',"")
    telefono = request.POST.get('telefono',0)
    region = request.POST.get('region',"")
    comuna = request.POST.get('comuna',"")
    tipo_vivienda = request.POST.get('mitipo',"")
    adoptante = Adoptante(correo=correo,run=run,nombre=nombre,fecha_n=fechan,telefono=telefono,region=region,comuna=comuna,tipo_vivienda=tipo_vivienda)
    adoptante.save()
    return HttpResponse('Adoptante Agregado'+'<br>  <br> <a href="http://127.0.0.1:8000/">Volver a menú</a>  '+ '<br>  <br> <a href="http://127.0.0.1:8000/registro/">Crear nuevo adoptante</a>   ')
    window.open('http://127.0.0.1:8000/','index.html')
  


def buscar(request,var):
    adoptante = Adoptante.objects.get(run=var)
    return HttpResponse('run:' + adoptante.run + '<br> nombre:' +adoptante.nombre + '<br> correo:' +adoptante.correo + '<br> Teléfono: '+ str(adoptante.telefono) + '<br> Fecha nac: '+ str(adoptante.fecha_n) + '<br> Región: '+ adoptante.region + '<br> Comuna: '+ adoptante.comuna + '<br> Tipo Vivienda: '+ adoptante.tipo_vivienda + 
    '<br>  <br> <a href="http://127.0.0.1:8000/">Atrás</a>')
    
def eliminar(request, var):
    adoptante = Adoptante.objects.get(run=var)
    adoptante.delete()
    return HttpResponse('Adoptante Eliminado'+ '<br>  <br> <a href="http://127.0.0.1:8000/">Volver al Menú</a>   ') 

def editar(request,var):
    adoptante = Adoptante.objects.get(run=var)
    return render(request, 'editar.html', {'adoptante': adoptante})
    return HttpResponse('Adoptante editado'+ '<br>  <br> <a href="http://127.0.0.1:8000/">Volver al Menú</a>   ')


def edicion(request, var):
    adoptante = Adoptante.objects.get(pk=var)

    correo = request.POST.get('email',0)
    run = request.POST.get('rut',0)
    nombre = request.POST.get('nombre',0)
    fechan = request.POST.get('fechan','')
    telefono = request.POST.get('telefono',0)
    region = request.POST.get('region','')
    comuna = request.POST.get('comuna','')
    tipo_vivienda = request.POST.get('mitipo','')

    
    adoptante.correo=correo
    adoptante.run = run
    adoptante.nombre = nombre
    adoptante.fecha_n = fechan
    adoptante.telefono = telefono
    adoptante.region = region
    adoptante.comuna = comuna
    adoptante.tipo_vivienda = tipo_vivienda

    adoptante.save()
    return HttpResponse('Adoptante Actualizado' + '<br>  <br> <a href="http://127.0.0.1:8000/">Volver al Menú</a>   ')
    
    

