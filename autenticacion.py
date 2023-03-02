from Validacion import Validacion

lista_usuarios = [{"nombre": "Esteban", "contrasena": "1234"}, {"nombre": "Alvaro", "contrasena": "4321"},
                  {"nombre": "Alejandro", "contrasena": "00023"}, {"nombre": "Johana", "contrasena": "78945"}]


class Autenticacion(Validacion):

    def __int__(self, validacionExtra):
        super().__init__(validacionExtra)

    def validar(self, peticion):
        for elements in lista_usuarios:
            if elements['nombre'] == peticion.nombre and elements['contrasena'] == peticion.contrasena:
                return peticion
            else:
                pass

    def obtenerUsuario(self, peticion):
        # Debo retornar un usuario si existe
        pass
