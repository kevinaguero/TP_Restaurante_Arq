from persona import Persona
from pedido import Pedido

class Cadete(Persona):
    def __init__(self, nombreCompleto, domicilio, telefono):
        super().__init__(nombreCompleto, domicilio, telefono)

    def tomarPedido(self, pedido):
        pedido.cadete = self
        pass

    def cambiarEstadoDelPedido(self, estado, pedido):
        pedido.estado = estado
        pass
