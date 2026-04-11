from MetodoPagamento import MetodoPagamento

class CartaoCredito(MetodoPagamento):
    def pagar(self, valor):
        print(f"Pagando R${valor} no cartão")