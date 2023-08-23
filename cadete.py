from persona import Persona
from restaurante import Pedido

class Cadete(Persona):
    def __init__(self, nombreCompleto, domicilio, telefono):
        super().__init__(nombreCompleto, domicilio, telefono)

    def tomarPedido(self, pedido):
        # Lógica para que el cadete tome el pedido
        pass

    def cambiarEstadoDelPedido(self, estado, pedido):
        # Lógica para cambiar el estado del pedido
        pass
