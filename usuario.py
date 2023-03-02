from abc import ABC


class Usuario(ABC):

    def __init__(self, nombre, contrasena):
        super().__init__(nombre, contrasena)

    def obtenerNombre(self):
        return self.nombre

    def obtenerContrasena(self):
        return self.contrasena