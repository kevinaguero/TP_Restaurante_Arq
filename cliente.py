from persona import Persona

class Cliente(Persona):
    def __init__(self, nombreCompleto, domicilio, telefono):
        super().__init__(nombreCompleto, domicilio, telefono)

    def solicitarPedido(self, restaurante, listaComidas):
        # Lógica para solicitar un pedido al restaurante
        pass

    def cancelarPedido(self, pedido):
        # Lógica para cancelar un pedido
        pass

    def mostrarInformacion(self):
        # Lógica para mostrar información del cliente
        pass
