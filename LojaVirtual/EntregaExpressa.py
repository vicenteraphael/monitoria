from TipoEntrega import TipoEntrega

class EntregaExpressa(TipoEntrega):
    def calcular_frete(self):
        return 25