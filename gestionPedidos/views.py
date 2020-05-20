from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from gestionPedidos.models import Clientes
from gestionPedidos.models import Botones
from django.core.mail import send_mail
from django.conf import settings
from gestionPedidos.forms import FormularioContacto
from gestionPedidos.forms import FormularioPrueba1
from gestionPedidos.forms import FormularioPrueba2
# Create your views here.

def busqueda_productos(request):

    return render(request, "busqueda_productos.html")

def buscar(request):

    if request.GET["prd"]:

        #mensaje="Articulo buscado: %r" %request.GET["prd"]
        
        producto= request.GET["prd"]

        if len(producto)>20:

            mensaje="Texto de busqueda demasiado largo"
        else:

            articulos=Articulos.objects.filter(nombre__icontains=producto)

            return render(request, "resultados_busqueda.html", {"articulos":articulos, "query":producto})

    else:

        mensaje="no hay el texto"

    return HttpResponse(mensaje)

def contacto (request):

    if request.method=="POST":
        
        miFormulario=FormularioContacto(request.POST)

        if miFormulario.is_valid():
            
            infForm=miFormulario.cleaned_data

            art=Clientes.objects.create(nombre=infForm['asunto'],email=infForm['email'],direccion=infForm['mensaje'])

            return render(request, "gracias.html")
    
    else:

        miFormulario=FormularioContacto()

    return render(request, "formulario_contacto.html", {"form":miFormulario})

        #subject=request.POST["asunto"]
        #abc=Clientes.objects.create(nombre=subject)
        #message=request.POST["mensaje"] +" "+ request.POST["email"]
        #email_from=settings.EMAIL_HOST_USER
        #recipient_list=["stephanyvalarezo@gmail.com"]
        #send_mail(subject, message, email_from, recipient_list)
          
        
        
        #return render (request, "gracias.html")

    #return render (request, "contacto.html")


def prueba1 (request):

    if request.method=="POST":
        
        miFormulario=FormularioPrueba1(request.POST)
        

        if miFormulario.is_valid():
            
            infForm=miFormulario.cleaned_data
            

            art=Botones.objects.filter(id=1).update(nombre=infForm['nombre'],estado=infForm['estado'])
          

            #return render(request, "resultados_busqueda.html", {"articulos":articulos, "query":producto})
            articulos2=Botones.objects.get(id=1)
            
            return render(request, "guardado.html",{"articulos2":articulos2,"form":miFormulario})

    else:

        miFormulario=FormularioPrueba1()
        

    return render(request, "prueba1.html", {"form":miFormulario})








