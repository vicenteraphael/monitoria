import Produto.ProdutoCompra as ProdutoCompra

class Carrinho:
    def __init__(self):
        self.__itens = []

    @property
    def itens(self):
        return self.__itens

    def adicionar(self, produto, quantidade):
        for item in self.itens:
            if (produto == item.produto):
                item.quantidade += quantidade
                return
        produto_compra = ProdutoCompra(produto, quantidade)
        self.itens.append(produto_compra)
        print("Adicionando ao carrinho:", produto_compra.produto)

    def remover(self, produto, quantidade=None):
        for item in self.itens:
            if (produto == item.produto):
                if (quantidade is None or quantidade >= item.quantidade):
                    self.itens.remove(item)
                else:
                    item.quantidade -= quantidade
                print(f"Removendo {produto}, quantidade = {quantidade}")
                return

        print(f"({produto}) não está no carrinho")

    def limpar(self):
        self.carrinho.clear()
        print("Esvaziando o carrinho...")

    def total(self):
        return sum(item.subtotal() for item in self.itens)
    
    def __repr__(self):
        if (len(self.itens) == 0): return "Carrinho vazio"

        desc = ""
        for item in self.itens:
            desc += repr(item) + "\n"

        return "Produtos do Carrinho:\n" + desc