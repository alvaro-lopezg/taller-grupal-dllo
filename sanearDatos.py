from Validacion import Validacion


class SanearDatos(Validacion):

    def __int__(self, validacionExtra):
        super().__init__(validacionExtra)

    def validar(self, peticion):
        peticion.set_nombre(peticion.nombre.strip())
        peticion.set_contrasena(peticion.contrasena.strip())
        peticion.set_direccionIP(peticion.direccionIP.strip())
        peticion.set_infoExtra(peticion.informacionExtraPeticion.strip())

        return peticion