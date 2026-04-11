from Produto import Produto

class ProdutoCompra:
    def __init__(self, produto: Produto, quantidade=1):
        self.produto = produto
        self.quantidade = quantidade

    def subtotal(self):
        return self.produto.preco_unitario * self.quantidade
    
    def mostrar(self):
        return f"ProdutoCompra: {self.produto.mostrar()}, quantidade={self.quantidade}"