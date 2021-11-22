from django.db import models
from django.contrib.auth.models import User
 
class Programar (models.Model):
    nombre=models.CharField(max_length=100,default=None,null=True)
    edad=models.IntegerField(default=None,null=True)
    destino=models.CharField(max_length=90,null=True)
    correo=models.EmailField( max_length=254,default=None,null=True)
    fecha=models.DateTimeField(null=True)
    personas=models.IntegerField(null=True)
    dias=models.IntegerField(null=True)
    comentario=models.TextField(default=None,null=True)
    identificacion=models.IntegerField(null=True) 
    presupuesto=models.IntegerField(null=True)
    
    


class Persona (models.Model):
    usuario=models.OneToOneField(User,  on_delete=models.CASCADE,default=None) 
    nombre=models.CharField(max_length=100,default=None)
    identificacion=models.IntegerField(primary_key=True,default=None)
    correo=models.EmailField( max_length=254,default=None)
    telefono=models.IntegerField(default=None)


class Contactar (models.Model):
    nombre=models.CharField(max_length=100)
    correo=models.EmailField(max_length=254, default=None )
    lugar=models.CharField(max_length=90)
    interes=models.TextField(max_length=90,default=None)
    

class Planear(models.Model):
     nombre=models.CharField(max_length=100,default=None,null=True)
     destino=models.CharField(max_length=90,null=True)
     correo=models.EmailField( max_length=254,default=None,null=True)
     comentario=models.TextField(default=None,null=True)


