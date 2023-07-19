#app/views.py

from unicodedata import name
from django.http import Http404
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from .models import FacturaPasajero, Pasajero, ServiciosPasajeros
from .forms import PasajeroForm, RegistroUsuarioForm, ServiciosForm, FacturaForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
# Create your views here.

# AQUI IMPORTAMOS LOS MODELOS Y FORMULARIOS, PARA DE ESTA FORMA NOS CREE CADA VISTA EN FORMATO HTML

# """ Crea vista del index """

def index(request):
    return render(request, "index.html")

#  -----------------------------------------------------------------  
# Crea vista del About

class AboutPageView(TemplateView):
    template_name= "componentes/about.html"

#  -----------------------------------------------------------------   
# Crea vista para el login

def loginUser(request):
    return render(request, "registration/loginUser.html")
#  -----------------------------------------------------------------  


# USUARIOS

@permission_required("app.content_type")
def administracion(request):
    return render(request, "adminUsers/administracion.html")
  
# Funcion para crear un nuevo usuario  
def registro(request):
    data = {
        "form": RegistroUsuarioForm()
    }
    # Se usa metodo "POST" para enviar el registro a la BD
    if request.method == "POST": 
        formulario = RegistroUsuarioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "¡Usuario Creado Correctamente!")
            return redirect(to="listadoUsuarios")     
        data["form"] = formulario
    return render(request, "registration/registro.html", data)
#  -----------------------------------------------------------------
# Funcion para solicitar a la BD el listado de usuarios creado a travez del metodo "GET"

def listadoUsuarios(request):
    listadoUsuarios = User.objects.all()
    
    page = request.GET.get("page", 1)
    
    try:
        paginator = Paginator(listadoUsuarios, 10)
        listadoUsuarios = paginator.page(page)
    except:
        raise Http404
        
    data = {
        "users": listadoUsuarios,
        "paginator": paginator
    }
    return render(request, "adminUsers/listadoUsuarios.html", data)

#  -----------------------------------------------------------------

def eliminarUsuario(request, id):
    usuario = get_object_or_404(User,id= id )
    usuario.delete()
    messages.success(request, "Registro Eliminado Correctamente")
    return redirect(to="listadoUsuarios")

#  -----------------------------------------------------------------

def editarUsuario(request, id):
    usuario = get_object_or_404(User, id=id)
    data = {
        "form": RegistroUsuarioForm(instance=usuario)
    } 
    if request.method == "POST":  
        formulario = RegistroUsuarioForm(data=request.POST,instance=usuario, files=request.FILES )
        if formulario.is_valid():
            formulario.save()   
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listadoUsuarios")
        data["form"] = formulario
    return render(request, "adminUsers/editarUsuario.html", data)


#  -----------------------------------------------------------------   
#PASAJEROS

def pasajeros(request):
    return render(request, "pasajeros/pasajeros.html")
#  -----------------------------------------------------------------   

def registroPasajero(request): 
    data = {
        "form": PasajeroForm()
    }
    if request.method == "POST":
        formulario = PasajeroForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro Guardado Correctamente")
            return redirect(to="listadoPasajeros")
        else:
            data["form"] = formulario
    
    return render(request, "pasajeros/registroPasajero.html", data)
    

#  -----------------------------------------------------------------   
def listadoPasajeros(request):
    listadoPasajeros = Pasajero.objects.all()
    
    page = request.GET.get("page", 1)
    
    try:
        paginator = Paginator(listadoPasajeros, 2)
        listadoPasajeros = paginator.page(page)
    except:
        raise Http404
        
    data = {
        "entity": listadoPasajeros,
        "paginator": paginator
    }
    return render(request, "pasajeros/listadoPasajeros.html", data)
    
#  -----------------------------------------------------------------   

def editarPasajero(request, rutOpasaporte):
    pasajero = get_object_or_404(Pasajero, rutOpasaporte=rutOpasaporte)
    data = {
        "form": PasajeroForm(instance=pasajero)
    } 
    if request.method == "POST":  
        formulario = PasajeroForm(data=request.POST,instance=pasajero, files=request.FILES )
        if formulario.is_valid():
            formulario.save()   
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listadoPasajeros")
        data["form"] = formulario
    return render(request, "pasajeros/editarPasajero.html", data)
#  -----------------------------------------------------------------   

def eliminarPasajero(request, id):
    pasajero = get_object_or_404(Pasajero, id=id)
    pasajero.delete()
    messages.success(request, "Registro Eliminado Correctamente")
    return redirect(to="listadoPasajeros")

#  -----------------------------------------------------------------   
#  -----------------------------------------------------------------   


#SERVICIOS

def serviciosPasajeros(request):
    data = {
        "form": ServiciosForm()
    }
    if request.method == "POST":
        formulario = ServiciosForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Servicio Guardado Correctamente")
            return redirect(to="listadoServicios")
        else:
            data["form"] = formulario
            
    return render(request, "servicios/servicios.html", data)
    

# ---------------------------------------------------------------------

def listadoServicios(request):
    listadoServicios = ServiciosPasajeros.objects.all()
    
    page = request.GET.get("page", 1)
    
    try:
        paginator = Paginator(listadoServicios, 2)
        listadoServicios = paginator.page(page)
    except:
        raise Http404
    data = {
        "entity": listadoServicios,
        "paginator": paginator
    }
    return render(request, "servicios/listadoServicios.html", data)
    
    
    # --------------------------------------------------------------------
def editarServicio(request, id):
    servicio = get_object_or_404(ServiciosPasajeros, id= id)
    data = {
        "form": ServiciosForm(instance=servicio)
    }
    if request.method == "POST":
        formulario = ServiciosForm(data=request.POST, instance=servicio, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Servicio Modificado Correctamente")
            return redirect(to=listadoServicios)
        data["form"] = formulario
    return render(request, "servicios/editarServicio.html", data)
    
    
    # ----------------------------------------------------------------------
    
def eliminarServicio(request, id):
    servicio = get_object_or_404(ServiciosPasajeros, id=id )
    servicio.delete()
    messages.success(request, "Registro Eliminado Correctamente")
    return redirect(to="listadoPasajeros")
    
    
 # ----------------------------------------------------------------------
 
 #FACTURA
def facturaPasajero(request):
    data = {
        "form": FacturaForm()
    }
    if request.method == "POST":
        formulario = FacturaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Factura Guardada Correctamente")
            return redirect(to="listadoFactura")
        else:
            data["form"] = formulario
            
    return render(request, "facturas/facturaPasajero.html", data)

# ----------------------------------------------------------------------

def listadoFactura(request):
    listadoFactura = FacturaPasajero.objects.all()
    
    page = request.GET.get("page", 1)
    
    try:
        paginator = Paginator(listadoFactura, 2)
        listadoFactura = paginator.page(page)
    except:
        raise Http404
    data = {
        "entity": listadoFactura,
        "paginator": paginator
    }
    return render(request, "facturas/listadoFacturas.html", data)
    
    
    # ----------------------------------------------------------------------
    """ Funcion para eliminar una factura """  
    
def eliminarFactura(request, id):
    
    """ Solicita el Objeto a la BD para su eliminacion """
    factura = get_object_or_404(FacturaPasajero, id=id ) 
    factura.delete()
    messages.success(request, "Factura Anulada Correctamente")
    return redirect(to="listadoPasajeros")
    
    
 # ----------------------------------------------------------------------
