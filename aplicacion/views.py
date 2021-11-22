from  django.contrib.auth.models import User
from django.contrib.messages.api import success, warning
from django.core.checks.messages import WARNING
from django.forms.forms import Form
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse
from aplicacion.models import*
from aplicacion.forms import*
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from datetime import date, datetime

    
def inicio(request):    
    return render( request,'inicio.html')

def miami (request):
    if request.method == "POST": 
        nombre = request.POST['nombre']
        correo = request.POST['correo']
        destino = request.POST['destino']
        comentario= request.POST['comentario']
        try:
            Planear.objects.create(nombre=nombre,  correo=correo, destino=destino,  comentario=comentario)
            messages=success(request,'muchas gracias, nos  pondremos en contacto contigo ')
        except:
            messages=warning(request,'ERROR')
        return render( request,'fav-miami.html')
        
    else:
        return render( request,'fav-miami.html')
    
def barranquilla (request):
    if request.method == "POST": 
        nombre = request.POST['nombre']
        correo = request.POST['correo']
        destino = request.POST['destino']
        comentario= request.POST['comentario']
        try:
            Planear.objects.create(nombre=nombre,  correo=correo, destino=destino,  comentario=comentario)
            messages=success(request,'muchas gracias, nos  pondremos en contacto contigo ')
        except:
            messages=warning(request,'ERROR')
        return render( request,'fav-barranquilla.html')
        
    else:
        return render( request,'fav-barranquilla.html')
         
def paris (request):
    if request.method == "POST": 
        nombre = request.POST['nombre']
        correo = request.POST['correo']
        destino = request.POST['destino']
        comentario= request.POST['comentario']
        try:
            Planear.objects.create(nombre=nombre,  correo=correo, destino=destino,  comentario=comentario)
            messages=success(request,'muchas gracias, nos  pondremos en contacto contigo ')
        except:
            messages=warning(request,'ERROR')
        return render( request,'fav-paris.html')
        
    else:
        return render( request,'fav-paris.html')
    

def medellin (request):
    if request.method == "POST": 
        nombre = request.POST['nombre']
        correo = request.POST['correo']
        destino = request.POST['destino']
        comentario= request.POST['comentario']
        try:
            Planear.objects.create(nombre=nombre,  correo=correo, destino=destino,  comentario=comentario)
            messages=success(request,'muchas gracias, nos  pondremos en contacto contigo ')
        except:
            messages=warning(request,'ERROR')
        return render( request,'fav-medellin.html')
        
    else:
        return render( request,'fav-medellin.html')
    

@login_required(login_url='/ingresar')
def programar (request):
    contexto = dict()
    programar=Programar.objects.all()
    for p in programar:
           p.presupuesto ='{:,}'.format(p.presupuesto).replace(',','.')
    contexto['programar'] = programar
    return render( request,'programar.html',contexto,)

@login_required(login_url='/ingresar')
def planear (request):
    if request.method == "POST": 
        pass
    else:
        return render( request,'planear.html')

@login_required(login_url='/ingresar')
def agregar (request):
    if request.method == "POST": 
        nombre = request.POST['nombre']
        identificacion = request.POST['identificacion']
        correo = request.POST['correo']
        edad = request.POST['edad']
        destino = request.POST['destino']
        fecha = request.POST['fecha']
        personas = request.POST['personas']
        dias = request.POST['dias']
        presupuesto = request.POST['presupuesto']
        comentario= request.POST['comentario']
        try:
            Programar.objects.create(nombre=nombre, identificacion= identificacion, correo=correo, edad=edad,destino=destino, fecha=fecha,personas=personas, dias=dias, presupuesto=presupuesto, comentario=comentario)
            messages=success(request,'Nos pondremos en contacto contigo para brindarte el mejor plan')
        except:
            messages=warning(request,'ERROR')
        return render( request,'agregar.html')

    else:
        return render (request, "agregar.html")

@login_required(login_url='/ingresar')
def editar (request,id):
    programar=Programar.objects.get(id=id)
    if request.method == "POST": 
        nombre = request.POST['nombre']
        identificacion = request.POST['identificacion']
        correo = request.POST['correo']
        edad = request.POST['edad']
        destino = request.POST['destino']
        fecha = request.POST['fecha']
        personas = request.POST['personas']
        dias = request.POST['dias']
        presupuesto = request.POST['presupuesto']
        comentario= request.POST['comentario']
        programar.nombre=nombre
        programar.identificacion=identificacion
        programar.correo=correo
        programar.edad=edad
        programar.destino=destino
        programar.fecha=fecha
        programar.personas=personas
        programar.dias=dias
        programar.presupuesto=presupuesto
        programar.comentario=comentario
        programar.save()
        try:
            messages=success(request,'DATOS EDITADOS ')
        except:
            messages=warning(request,'ERROR')
            return render( request,'editar.html')
        return render (request,'editar.html',{'programar':programar})
    else:
        return render (request,'editar.html',{'programar':programar})

@login_required(login_url='/ingresar')
def eliminar (request,id):
    dato=Programar.objects.get(id=id)
    dato.delete()
    messages=success(request,'DATOS ELIMINADOS ')
    return render (request,'programar.html')
    

def registrar_user (request):
    if request.method == 'POST':
        form = Usuarioform(request.POST)
        if form.is_valid():
            usuario= form.cleaned_data['usuario']
            correo= form.cleaned_data['correo']
            password1= form.cleaned_data['password1']
            password2= form.cleaned_data['password2']
            if password1 == password2:
                User.objects.create_user(usuario , correo, password1)
                messages=success(request,'USUARIO CREADO')
                return redirect (reverse('registrarce'))
            else:
                 messages=warning(request,'LAS CONTRASEÑAS NO COINCIDEN  ')
                 return redirect (reverse('registrarce'))
        else:
                 messages=warning(request,' DATOS  INCORRECTOS ')
                 return redirect (reverse('registrarce'))
    else:
        contexto=dict()
        contexto['Usuarioform'] = Usuarioform()
        return render(request,'registrar.html',contexto)

def ingresar (request):
    if request.method == 'POST':
        entrar= Entrarform(request.POST)
        if entrar.is_valid():
            usuario= entrar.cleaned_data['usuario']
            password= entrar.cleaned_data['password']
            ingreso = authenticate(username=usuario, password=password)
            if ingreso is  not None:
                 login(request,ingreso)
                 return redirect (reverse('programar'))
            else:
                 messages=warning(request,'DASTOS INVALIDOS  ')
                 return redirect (reverse('ingresar'))
        else :
            messages=warning(request,'DASTOS INVALIDOS  ')
            return redirect (reverse('ingresar'))
    else:
        contexto=dict()
        contexto['formEntrar'] = Entrarform()
        return render(request,'ingresar.html',contexto ) 

@login_required(login_url='/ingresar')
def salir (request):
    logout(request)
    return redirect (reverse('inicio'))

def noticias(request):
    return render (request,'noticias.html')


def paquetes (request):
    return render (request,'paquetes.html')
           
 
     



 

