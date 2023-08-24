# main.py
from domicilio import *
from cliente import *
from cadete import *
from comida import *
from restaurante import *

# Crear una instancia de la clase Domicilio
domicilio_persona = Domicilio(calle="Calle Principal", numero="123", zona="Sur", ciudad="Ciudad Ejemplo", correoPostal="4723")

# Crear una instancia de la clase Persona
persona = Persona(nombreCompleto="Juan Pérez", domicilio=domicilio_persona, telefono="123-456-7890")

# Acceder a los atributos de la instancia de Persona
print("# Acceder a los atributos de la instancia de Persona")
print("Nombre:", persona.nombreCompleto)
print("Teléfono:", persona.telefono)
print("Domicilio:", persona.domicilio.calle, persona.domicilio.numero, persona.domicilio.zona, persona.domicilio.ciudad, persona.domicilio.correoPostal)

# Mostrar informacion de un Cliente
print("\n# Mostrar informacion de un Cliente")
cliente = Cliente(nombreCompleto="Kevin Aguero", domicilio=domicilio_persona, telefono="123-456-7890")
cliente.mostrarInformacion()

# Consultar disponibilidad de Restaurante
print("\n# Consultar disponibilidad de Restaurante")
comida1 = Comida(nombre="Milanesa de carne", descripcion="Milanesa de carne al plato", precio = 1000.00)
comida2 = Comida(nombre="Milanesa de merluza", descripcion="Milanesa de merluza al plato", precio = 800.00)
menuRestaurante = [comida1, comida2]
restaurante = Restaurante(nombre="La Mila Potente", descripcion="Restaurante especializado en milanesas", direccion="Calle Siempreviva 742", menu=menuRestaurante, disponibilidad=True)

restaurante.consultarDisponibilidad()

# Consultar comidas de Restaurante
print("\n# Consultar comidas de Restaurante")
restaurante.consultarComidas()

# Solicitar pedido (Cliente)
listaComidas = []
for comida in restaurante.consultarComidas():
    listaComidas.append(comida)

pedido = cliente.solicitarPedido(restaurante=restaurante, listaComidas=listaComidas)

# Calcular precio total del pedido (Pedido)
print("\n# Calcular precio total del pedido")
precioPedido = pedido.calcularPrecioTotal()
print(precioPedido)

# Tomar pedido (Cadete)
print("\n# Tomar pedido (Cadete)")
cadete = Cadete(nombreCompleto="Gustavo Contreras", domicilio=domicilio_persona, telefono="123-456-7890")
cadete.tomarPedido(pedido=pedido)
print(pedido.cadete.nombreCompleto)

# Cambiar estado del pedido (Cadete)
print("\n# Cambiar estado del pedido (Cadete)")
cadete.cambiarEstadoDelPedido(estado="Preparado", pedido=pedido)
print(pedido.estado)

# Cancelar pedido (Cliente)
print("\n# Cancelar pedido (Cliente)")
cliente.cancelarPedido(pedido=pedido)
print(pedido.estado)

# Agregar comida a un pedido (Pedido)
print("\n# Agregar comida a un pedido (Pedido)")
comida3 = Comida(nombre="Milanesa de pollo", descripcion="Milanesa de pollo al plato", precio = 1100.00)
pedido.agregarComida(comida=comida3)
for indice in range(len(listaComidas)):
    print(pedido.listaComidas[indice])

# Eliminar comida a un pedido (Pedido)
print("\n# Eliminar comida a un pedido (Pedido)")
pedido.eliminarComida(comida=comida3)
for indice in range(len(listaComidas)):
    print(pedido.listaComidas[indice])
