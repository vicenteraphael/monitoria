import MetodoPagamento.MetodoPagamento as MetodoPagamento

class Boleto(MetodoPagamento):
    def pagar(self, valor):
        print(f"Gerando boleto de R${valor}")