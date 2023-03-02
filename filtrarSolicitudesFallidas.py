from Validacion import Validacion

lista_solicitudes_fallidas = [{"nombre": "Esteban", "direccionIP": "10.0.0.16"}]


class FiltrarSolicitudesFallidas(Validacion):

    def __int__(self, validacionExtra):
        super().__init__(validacionExtra)

    def validar(self, peticion):
        self.obtenerSolicitudFallida(peticion.nombre, peticion.contrasena, peticion.direccionIP)

    def crearSolicitudFallida(self,nueva_solicitud):
        lista_solicitudes_fallidas.append(nueva_solicitud)

    def obtenerSolicitudFallida(self, nombre, direccionIP):
        for elements in lista_solicitudes_fallidas:
            if elements['nombre'] == nombre and elements['direccionIP'] == direccionIP:
                return elements
            else:
                fallida = {"nombre":elements['nombre'], "direccionIP": elements[direccionIP]}
                self.crearSolicitudFallida(fallida)

