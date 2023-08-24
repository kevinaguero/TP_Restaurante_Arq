class Comida:
    def __init__(self, nombre, descripcion, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

    def __str__(self):
        ...
        return f"Plato: {self.nombre}. Descripcion: {self.descripcion}. Precio: {self.precio}"
