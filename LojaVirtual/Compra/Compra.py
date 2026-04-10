import Pessoa.Cliente as Cliente, MetodoPagamento.MetodoPagamento as MetodoPagamento, Entrega.Entrega as Entrega

class Compra:
    def __init__(self, usuario: Cliente, pagamento: MetodoPagamento, entrega: Entrega):
        self.usuario = usuario
        self.carrinho = usuario.carrinho
        self.pagamento = pagamento
        self.entrega = entrega
        
    def total(self):
        total_produtos = self.carrinho.total() + self.entrega.calcular_frete()
        frete = self.entrega.calcular_frete()
        return total_produtos + frete

    def finalizar(self):
        valor = self.total()
        self.pagamento.pagar(valor)
        print("Compra finalizada!")