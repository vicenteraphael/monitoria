import Produto.Produto as Produto

class ProdutoCompra:
    def __init__(self, produto: Produto, quantidade=1):
        self.produto = produto
        self.quantidade = quantidade

    def subtotal(self):
        return self.produto.preco_unitario * self.quantidade
    
    def __repr__(self):
        return f"ProdutoCompra: {repr(self.produto)}, quantidade={self.quantidade}"