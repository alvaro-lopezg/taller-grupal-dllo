from Validacion import Validacion


class CachePeticiones(Validacion):

    def __int__(self, validacionExtra):
        super().__init__(validacionExtra)

    def validar(self, peticion):
        print("En este metodo se verifica si la validacion que se esa intentando realizar ya fue realizada "
              "anteriormente, para responder mas rapido")
        """Usando la clase CacheUsuariosLogueados, se busca en cache si la peticion ya se hizo previamente
            si la peticion no existe entonces se agrega en cache para posteriores consultas
        """

        return peticion