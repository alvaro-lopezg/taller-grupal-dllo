

class Peticion:

    def __int__(self, nombre, contrasena, direccionIP, informacionExtraPeticion):
        self.nombre = nombre
        self.contrasena = contrasena
        self.direccionIP = direccionIP
        self.informacionExtraPeticion = informacionExtraPeticion

    def get_nombre(self):
        return self.nombre

    def get_contrasena(self):
        return self.contrasena

    def get_direccionIP(self):
        return self.direccionIP

    def get_infoExtra(self):
        return self.informacionExtraPeticion

    #Setter
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_contrasena(self, contrasena):
        self.contrasena = contrasena

    def set_direccionIP(self, direccionIP):
        self.direccionIP = direccionIP

    def set_infoExtra(self,informacionExtraPeticion ):
        self.informacionExtraPeticion = informacionExtraPeticion