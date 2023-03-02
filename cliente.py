from usuario import Usuario


class Cliente(Usuario):
    """ La clase clente hereda de usuario """

    def __init__(self, nombre, contrasena):
        super().__init__(nombre, contrasena)

    def crearOrden(self):
        pass