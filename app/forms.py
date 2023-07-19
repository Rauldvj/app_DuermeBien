from dataclasses import field, fields
from datetime import date
from pyexpat import model
from django import forms
from django.forms import widgets
from .models import FacturaPasajero, Pasajero, ServiciosPasajeros
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# AQUI IMPORTAMOS LOS MODELOS Y GRACIAS AL REST FRAMEWORK, CREAMOS LOS FORMULARIOS

class PasajeroForm(forms.ModelForm):
    class Meta:
        widget = {"llegada": forms.DateInput(attrs={"type": date})}
        widget = {"salida": forms.DateInput(attrs={"type": date})}
        model = Pasajero
        fields= "__all__"
        
    
class RegistroUsuarioForm(UserCreationForm):  
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password1", "password2"]
        
        
class ServiciosForm(forms.ModelForm):
    class Meta:
        model = ServiciosPasajeros
        fields = "__all__"
        
class FacturaForm(forms.ModelForm):
    class Meta:
        model = FacturaPasajero
        fields = "__all__"