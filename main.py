# main.py
from persona import *
from domicilio import *

# Crear una instancia de la clase Domicilio
domicilio_persona = Domicilio(calle="Calle Principal", numero="123", ciudad="Ciudad Ejemplo", pais="País Ejemplo")

# Crear una instancia de la clase Persona
persona = Persona(nombreCompleto="Juan Pérez", domicilio=domicilio_persona, telefono="123-456-7890")

# Acceder a los atributos de la instancia de Persona
print("Nombre:", persona.nombreCompleto)
print("Teléfono:", persona.telefono)
print("Domicilio:", persona.domicilio.calle, persona.domicilio.numero, persona.domicilio.zona, persona.domicilio.ciudad, persona.domicilio.correoPostal)
