from rest_framework import generics
from app.models import Pasajero, ServiciosPasajeros, FacturaPasajero
from .serializers import PasajeroSerializer, ServiciosPasajerosSerializer, FacturaPasajeroSerializer

class PasajeroAPIView(generics.ListCreateAPIView):
    queryset = Pasajero.objects.all()
    serializer_class = PasajeroSerializer
    
class ServiciosPasajerosAPIView(generics.ListCreateAPIView):
    queryset = ServiciosPasajeros.objects.all()
    serializer_class = ServiciosPasajerosSerializer
    
class FacturaPasajerosAPIView(generics.ListCreateAPIView):
    queryset = FacturaPasajero.objects.all()
    serializer_class = FacturaPasajeroSerializer
    
    
class DetailPasajero(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pasajero.objects.all()
    serializer_class = PasajeroSerializer
    
class DetailServicios(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiciosPasajeros.objects.all()
    serializer_class = ServiciosPasajerosSerializer

class DetailFacturas(generics.RetrieveUpdateDestroyAPIView):
    queryset = FacturaPasajero.objects.all()
    serializer_class = FacturaPasajeroSerializer
    

