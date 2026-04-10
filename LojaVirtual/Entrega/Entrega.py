from abc import ABC, abstractmethod

class Entrega(ABC):
    @abstractmethod
    def calcular_frete():
        pass