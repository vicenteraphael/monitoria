from Cliente import Cliente
from MetodoPagamento import MetodoPagamento
from TipoEntrega import TipoEntrega
from Estoque import Estoque

class Compra:
    def __init__(self, cliente: Cliente, pagamento: MetodoPagamento, entrega: TipoEntrega, estoque: Estoque):
        self.cliente = cliente
        self.carrinho = cliente.carrinho
        self.pagamento = pagamento
        self.entrega = entrega
        self.estoque = estoque

    def validar(self):
        for item in self.carrinho.itens:
            if not self.estoque.tem_estoque(item.produto):
                raise ValueError("Estoque insuficiente")
        
    def total(self):
        total_produtos = self.carrinho.total()
        frete = self.entrega.calcular_frete()
        return total_produtos + frete

    def finalizar(self):
        self.validar()
        valor = self.total()
        self.pagamento.pagar(valor)
        print("Compra finalizada!")