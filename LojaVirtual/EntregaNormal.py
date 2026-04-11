from TipoEntrega import TipoEntrega

class EntregaNormal(TipoEntrega):
    def calcular_frete(self):
        return 10