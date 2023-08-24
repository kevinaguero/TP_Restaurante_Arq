from persona import Persona
from pedido import Pedido

class Cliente(Persona):
    def __init__(self, nombreCompleto, domicilio, telefono):
        super().__init__(nombreCompleto, domicilio, telefono)

    def solicitarPedido(self, restaurante, listaComidas):
        pedido = Pedido(cliente=self, restaurante=restaurante, listaComidas=listaComidas, estado="En preparacion")
        return pedido

    def cancelarPedido(self, pedido):
        pedido.estado = "Cancelado"
        pass

    def mostrarInformacion(self):
        print(f"Nombre completo: {self.nombreCompleto}")
        print(f"Domicilio: Calle {self.domicilio.calle} {self.domicilio.numero} en zona {self.domicilio.zona} en la ciudad {self.domicilio.ciudad} con codigo postal {self.domicilio.correoPostal}")
        print(f"Telefono: {self.telefono}")
        pass
