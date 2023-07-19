from tabnanny import verbose
from django.db import models

# AQUI CREAMOS LOS MODELOS QUE NOS SERVIRAN PARA CREAR LAS TABLAS (DJANGO AL REALIZAR EL MAKEMIGRATION, NOS CREA
# AUTOMATICAMENTE LAS TABLAS EN SQL)

# Create your models here.

#MODELO PARA PASAJEROS
class Pasajero(models.Model):
    rutOpasaporte = models.CharField(max_length=30, verbose_name="Rut o Pasaporte")
    nombres = models.CharField(max_length=200, verbose_name="Nombres")
    apellidos = models.CharField(max_length=200, verbose_name="Apellidos")
    direccion = models.CharField(max_length=300, verbose_name="Direccion")
    email = models.CharField(max_length=100, verbose_name="Email")
    telefono = models.CharField(max_length=50, verbose_name="Telefono")
    pais = models.CharField(max_length=100, verbose_name="Pais")
    ciudad = models.CharField(max_length=100, verbose_name="Ciudad")
    
    opciones_numero = [
        ["101", "101"],
        ["102", "102"],
        ["103", "103"],
        ["204", "204"],
        ["205", "205"],
        ["206", "206"],
        ["307", "307"],
        ["308", "308"],
        ["309", "309"],
    ]
    nHabitacion = models.CharField(max_length=50, choices=opciones_numero, verbose_name="Numero Habitacion")
    # ---------------------------
    opciones_tipo = [ 
        ["Single", "Single"],
        ["Doble", "Doble"],
        ["Queen", "Queen"],
        ["King", "King"],
    ]
    tipoHabitacion = models.CharField(max_length=50, choices=opciones_tipo, verbose_name="Tipo de Habitacion")
    # ---------------------------
    cantidadNinos = models.PositiveIntegerField(default=0, verbose_name="Cantidad Niños")
    cantidadAdultos = models.PositiveIntegerField(default=0, verbose_name="Cantidad Adultos")
    llegada = models.DateField(verbose_name="Llegada")
    salida = models.DateField(verbose_name="Salida")
    
    def __str__(self):
        return ""+ ""+ self.rutOpasaporte + ", " + " " + self.nombres + " " + self.apellidos
        
        
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

##MODELO  SERVICIOS PASAJEROS

class ServiciosPasajeros(models.Model):
    dni= models.ForeignKey(Pasajero, on_delete=models.CASCADE, max_length=50, verbose_name="DNI")
    
    opciones_telefoniaFull = [ 
        ["No Desea", "No Desea"],
        ["Telenofia Full", "Telefonia Full"],
    ]
    telefoniaFull = models.CharField(max_length=50, choices=opciones_telefoniaFull, default="No Desea", verbose_name="Telefonia Full")
    
    # -------------------------------------------------------------------------------------------------------
    opciones_telefoniaLocal = [ 
        ["No Desea", "No Desea"],
        ["Telefonia Local", "Telefonia Local"]
    ]
    telefoniaLocal = models.CharField(max_length=50, choices=opciones_telefoniaLocal, default="No Desea", verbose_name="Telefonia Local")
    # -------------------------------------------------------------------------------------------------------
    
    opciones_desayuno = [ 
        ["No Desea", "No Desea"],
        ["Desayuno", "Desayuno"]
    ]
    desayuno = models.CharField(max_length=50, choices=opciones_desayuno,default="No Desea", verbose_name="Desayuno")
    
    # -------------------------------------------------------------------------------------------------------
    opciones_almuerzo = [ 
        ["No Desea", "No Desea"],
        ["Almuerzo", "Almuerzo"],
    ]
    almuerzo = models.CharField(max_length=50, choices=opciones_almuerzo,default="No Desea", verbose_name="Almuerzo")
    # -------------------------------------------------------------------------------------------------------
    opciones_cena = [ 
        ["No Desea", "No Desea"],
        ["Cena", "Cena"],
    ]
    cena = models.CharField(max_length=50, choices=opciones_cena,default="No Desea", verbose_name="Cena")
    # -------------------------------------------------------------------------------------------------------
    
    opciones_barra = [ 
        ["No Desea", "No Desea"],
        ["Barra Libre", "Barra Libre"],
    ]
    bar = models.CharField(max_length=50, choices= opciones_barra, default="No Desea", verbose_name="Bar")
    # -------------------------------------------------------------------------------------------------------
    opciones_minibar = [ 
        ["No Desea", "No Desea"],
        ["Mini Bar", "Mini Bar"],
    ]
    miniBar = models.CharField(max_length=50, choices= opciones_minibar, default="No Desea", verbose_name="Mini Bar")
     # -----------------------------------------------------------
     
    opciones_lavanderia = [ 
        ["No Desea", "No Desea"],
        ["Lavanderia", "Lavanderia"],
    ]
    lavanderia= models.CharField(max_length=50, choices=opciones_lavanderia, default="No Desea", verbose_name="Lavanderia")
    
     # -----------------------------------------------------------
     
    opciones_planchado = [ 
        ["No Desea", "No Desea"],
        ["Planchado", "Planchado"],
    ]
    planchado = models.CharField(max_length=50, choices=opciones_planchado, default="No Desea", verbose_name="Planchado")
    
     # -----------------------------------------------------------
     
    def __str__(self):
        lista = "Telefonia Full: " + self.telefoniaFull + "Telefonia Local: " + self.telefoniaLocal + "Desayuno: " + self.desayuno + "Almuerzo: " + self.almuerzo + "Cena: " + self.cena + " Bar: " + self.bar + "Mini Bar: " + self.miniBar + "Lavanderia: " + self.lavanderia + "Planchado: " + self.planchado
        return lista
        
# ----------------------------------------------------------------------------------------------------

#MODELO FACTURA

class FacturaPasajero(models.Model):
    pasajero = models.ForeignKey(Pasajero, on_delete=models.CASCADE, max_length=50, verbose_name="Pasajero")
    servicios= models.ForeignKey(ServiciosPasajeros, on_delete=models.CASCADE, max_length=50, verbose_name="Servicios")  
    total = models.PositiveBigIntegerField(default=0, verbose_name="Valor Total")
    opciones_pago = [ 
        ["efectivo", "efectivo"],
        ["Debito", "Debito"],
        ["Tarjeta Credito", "Tarjeta Credito"]
    ]
    formaPago = models.CharField(max_length=50, choices=opciones_pago, default="No Desea", verbose_name="Forma Pago")
    

    