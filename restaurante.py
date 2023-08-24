class Restaurante:
    def __init__(self, nombre, descripcion, direccion, menu, disponibilidad):
        self.nombre = nombre
        self.descripcion = descripcion
        self.direccion = direccion
        self.menu = menu
        self.disponibilidad = disponibilidad

    def consultarDisponibilidad(self):
        # Lógica para consultar la disponibilidad del restaurante
        return self.disponibilidad
        pass

    def consultarComidas(self):
        return self.menu
        pass
