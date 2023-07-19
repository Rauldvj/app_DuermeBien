from rest_framework import serializers
from app.models import Pasajero, ServiciosPasajeros, FacturaPasajero

class PasajeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pasajero
        fields = "__all__"
        
class ServiciosPasajerosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiciosPasajeros
        fields = "__all__"
       
class FacturaPasajeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacturaPasajero
        fields = "__all__"
