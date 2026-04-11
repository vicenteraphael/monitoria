from abc import ABC, abstractmethod

class TipoEntrega(ABC):
    @abstractmethod
    def calcular_frete():
        pass