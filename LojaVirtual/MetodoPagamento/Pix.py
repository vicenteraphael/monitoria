import MetodoPagamento.MetodoPagamento as MetodoPagamento

class Pix(MetodoPagamento):
    def pagar(self, valor):
        print(f"Pagando R${valor} via PIX")