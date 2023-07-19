from django.contrib import admin
from .models import Pasajero, ServiciosPasajeros, FacturaPasajero

class PasajeroAdmin(admin.ModelAdmin):
    list_display = ["id", "rutOpasaporte", "nombres", "apellidos", "telefono", "llegada", "salida", "nHabitacion"]
    search_fields = ["rutOpasaporte"]
    
class ServiciosAdmin(admin.ModelAdmin):
    list_display = ["id", "dni", "telefoniaFull", "telefoniaLocal", "desayuno", "almuerzo", "cena", "bar", "miniBar", "lavanderia", "planchado"]
    search_fields = ["dni"]
    
class FacturaAdmin(admin.ModelAdmin):
    list_display = "pasajero", "servicios", "total", "formaPago"
    search_fields = ["pasajero"]
    

# Register your models here.

admin.site.register(Pasajero, PasajeroAdmin)
admin.site.register(ServiciosPasajeros, ServiciosAdmin)
admin.site.register(FacturaPasajero, FacturaAdmin)
