from django.urls import path
from . import views
from .views import AboutPageView
from api.views import PasajeroAPIView, ServiciosPasajerosAPIView, FacturaPasajerosAPIView, DetailPasajero, DetailServicios, DetailFacturas

urlpatterns = [ 
        #URLS LOGIN
    path("", views.index, name="index"),
    path("loginUser/", views.login, name="loginUser"),
    path("about/", AboutPageView.as_view(), name="about"),
    # ---------------------------------------------------------------------------------------------------
    #URLS PASAJEROS
    path("pasajeros/", views.pasajeros, name="pasajeros"),
    path("registroPasajero/", views.registroPasajero, name="registroPasajero"),
    path("listadoPasajeros/", views.listadoPasajeros, name="listadoPasajeros"),
    path("editarPasajero/<rutOpasaporte>/", views.editarPasajero, name="editarPasajero"),
    path("eliminarPasajero/<id>/", views.eliminarPasajero, name="eliminarPasajero"),
    
    #URLS ADMINISTRACION USER
    path("administracion/", views.administracion, name="administracion"),
    path("registro/", views.registro, name="registro"),
    path("listadoUsuarios/", views.listadoUsuarios, name="listadoUsuarios"),
    path("editarUsuario/<id>", views.editarUsuario, name="editarUsuario"),
    path("eliminarUsuario/<id>/", views.eliminarUsuario, name="eliminarUsuario"),
    
    # ---------------------------------------------------------------------------------------------------
    #SERVICIOS
    path("servicios/", views.serviciosPasajeros, name="servicios"),  
    path("listadoServicios/", views.listadoServicios, name="listadoServicios"),
    path("editarServicio/<id>", views.editarServicio, name="editarServicio"),
    path("eliminarServicio/<id>/", views.eliminarServicio, name="eliminarServicio"),
    
     # ---------------------------------------------------------------------------------------------------
     #FACTURA
    path("facturaPasajero/", views.facturaPasajero, name="facturaPasajero"),  
    path("listadoFactura/", views.listadoFactura, name="listadoFactura"),
     path("eliminarFactura/<id>/", views.eliminarFactura, name="eliminarFactura"),

     
    # ---------------------------------------------------------------------------------------------------
     #APIS
    path("pasajerosAPI", PasajeroAPIView.as_view(), name="PasajerosAPI"),
    path("DetailPasajerosAPI/<int:pk>/", DetailPasajero.as_view(), name="DetailPasajerosAPI"),
    path("serviciosAPI", ServiciosPasajerosAPIView.as_view(), name="serviciosAPI"),
    path("DetailServiciosAPI/<int:pk>/", DetailServicios.as_view(), name="DetailServiciosAPI"),
    path("facturasAPI", FacturaPasajerosAPIView.as_view(), name="facturasAPI"),
    path("DetailPFacturasAPI/<int:pk>/", DetailFacturas.as_view(), name="DetailFacturasAPI"),
]