from django.urls import path
from .views import PasajeroAPIView, ServiciosPasajerosAPIView, FacturaPasajerosAPIView, DetailPasajero, DetailServicios, DetailFacturas

urlpatterns = [ 
    path("pasajerosAPI", PasajeroAPIView.as_view(), name="PasajerosAPI"),
    path("DetailPasajerosAPI/<int:pk>/", DetailPasajero.as_view(), name="DetailPasajerosAPI"),
   
]