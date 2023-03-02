from abc import ABC, abstractmethod


class Validacion(ABC):

    def __int__(self, validacionExtra):
        super().__init__(validacionExtra)

    @abstractmethod
    def validar(self, peticion):
        pass

