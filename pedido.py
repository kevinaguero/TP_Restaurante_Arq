from datetime import datetime

class Pedido:
    def __init__(self, cliente, restaurante, listaComidas, estado):
        self.cliente = cliente
        self.restaurante = restaurante
        self.listaComidas = listaComidas
        self.estado = estado
        self.cadete = None
        self.fechaPedido = datetime.now()

    def calcularPrecioTotal(self):
        total = sum(comida.precio for comida in self.listaComidas)
        return total

    def agregarComida(self, comida):
        self.listaComidas.append(comida)

    def eliminarComida(self, comida):
        self.listaComidas.remove(comida)
