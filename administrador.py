from usuario import Usuario


class Administrador(Usuario):

    def __init__(self, nombre, contrasena):
        super().__init__(nombre, contrasena)

    def crearOden(self):
        pass

    def actualizarOrden(self):
        pass

    def obtenerOrden(self):
        pass

    def eliminarOrden(self):
        pass